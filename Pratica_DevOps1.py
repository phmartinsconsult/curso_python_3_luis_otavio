
resource "random_password" "password" {
  length           = 16
  special          = false
  override_special = "_%@"
}

resource "vault_generic_secret" "credentials" {
  path = "secret/databases/postgres/${var.environment}"


  data_json = <<EOT
{
  "username":   "root",
  "password": "${random_password.password.result}",
  "host": "${module.db.db_instance_address}"
}
EOT
