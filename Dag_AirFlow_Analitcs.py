from airflow.models import Variable
from utils.utils import read_files_from_s3, read_data_as_yaml
from airflow.decorators import dag, task
from airflow.utils.task_group import TaskGroup
from sensors.smart_emr_step_sensor import SmartEmrStepSensor

from typing import List, Dict, Union
from airflow.providers.amazon.aws.operators.emr_terminate_job_flow import (
    EmrTerminateJobFlowOperator
)
from airflow.providers.amazon.aws.operators.emr_create_job_flow import (
    EmrCreateJobFlowOperator
)
from airflow.contrib.operators.emr_add_steps_operator import (
    EmrAddStepsOperator
)
from airflow import DAG
from airflow.utils.dates import days_ago

from dag_utils.emr import create_emr_task_group
from dag_utils import nimbus

from datetime import datetime, timedelta
import json
import os
import random
import sys

sys.path.append('/opt/airflow/plugins')

artifacts_bucket = os.environ['artifacts_bucket']

DAG_ID = os.path.basename(__file__).replace(".py", "")
DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
}
DAG_TAGS = ["emr"]

dag_definition = {
    "dag_id": DAG_ID,
    "description": "Run built-in Spark app on Amazon EMR",
    "default_args": DEFAULT_ARGS,
    "dagrun_timeout": timedelta(hours=2),
    "start_date": days_ago(1),
    "schedule_interval": None,
    "concurrency": 7,
    "tags": DAG_TAGS,
    "catchup": False
}

s3_path = f"s3://{artifacts_bucket}/jobs/analytics_pipeline/ymls/emr_instance_groups.yml"
s3_file = read_files_from_s3(s3_path)
params = read_data_as_yaml(s3_file)
JOB_FLOW_OVERRIDES = {
    "Name": params["job_name"],
    "LogUri": params["log_path_s3"],
    "ReleaseLabel": params["emr_version"],
    "StepConcurrencyLevel": params["step_concurrency_level"],
    "VisibleToAllUsers": params["visible_to_all_users"],
    "JobFlowRole": params["job_flow_role"],
    "ScaleDownBehavior": params["scale_down_behavior"],
    "ServiceRole": params["service_role"],
    "EbsRootVolumeSize": params["ebs_root_volume_size"],
    "Tags": params["tags"],
    "Configurations": params["configurations"],
    "Applications": params["applications"],
    "Steps": params["steps"],
    "Instances": params["instances"],
    "BootstrapActions": params["bootstrap_actions"],
}


@dag(**dag_definition)
def pre_analytics_pipeline():
    cluster_creator = EmrCreateJobFlowOperator(
        task_id="create_job_flow",
        aws_conn_id="aws_default",
        job_flow_overrides=JOB_FLOW_OVERRIDES
    )

    cluster_terminator = EmrTerminateJobFlowOperator(
        task_id="terminate_emr_cluster",
        job_flow_id="{{ task_instance.xcom_pull(task_ids='create_job_flow', key='return_value') }}",
        aws_conn_id="aws_default",
        trigger_rule="all_done",
        retries=3,
        retry_delay=timedelta(seconds=60)
    )

    s3_path = f"s3://{artifacts_bucket}/jobs/analytics_pipeline/ymls/table_configuration.yml"

    s3_file = read_files_from_s3(s3_path)
    job_definition = read_data_as_yaml(s3_file)['batch_steps']

    layer_one = job_definition.get("layer_one")
    layer_two = job_definition.get("layer_two")
    layer_three = job_definition.get("layer_three")

    all_steps = layer_one + layer_two + layer_three

    golden_records = create_emr_task_group(
        steps=layer_one,
        task_group="golden_records",
        trigger_rule="all_success"
    )

    tg1_metadata_aggregator_steps = nimbus.create_metadata_aggregator_steps(layer_one)
    tg1_metadata_aggregator = create_emr_task_group(
        steps=tg1_metadata_aggregator_steps,
        task_group="layer_one_metadata_aggregator",
        trigger_rule="one_success"
    )

    obts = create_emr_task_group(
        steps=layer_two,
        task_group="one_big_tables",
        trigger_rule="all_success"
    )

    historical_materializer = create_emr_task_group(
        steps=layer_three,
        task_group="historical_materializer",
        trigger_rule="all_success"
    )
    metadata_aggregator_steps = nimbus.create_metadata_aggregator_steps(all_steps)
    metadata_aggregator_steps.extend(nimbus.create_data_preview_steps(all_steps))
    metadata_aggregator = create_emr_task_group(
        steps=metadata_aggregator_steps,
        task_group=f"metadata_aggregator",
        trigger_rule="one_success"
    )

    house_cleaning_steps = nimbus.house_cleaning_steps_creator(all_steps)
    house_cleaning = create_emr_task_group(
        steps=house_cleaning_steps,
        task_group=f"house_cleaning",
        trigger_rule="one_success"
    )

    cluster_creator >> golden_records >> tg1_metadata_aggregator >> obts >> historical_materializer >> metadata_aggregator >> house_cleaning >> cluster_terminator


dag = pre_analytics_pipeline()
