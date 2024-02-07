provider "google" {
  project     = var.project_id
  region      = var.region
}

# Create bucket composer
resource "google_storage_bucket" "create_bucket" {
  name                        = var.bucket_name_composer
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = false
}

# Create service account composer
resource "google_service_account" "sa_composer" {
  account_id   = var.sa_composer_name
  display_name = "Create Service Account for Composer Environment"
}
# Attach role worker in service account composer
resource "google_project_iam_member" "attach_role_composer-worker" {
  project = var.project_id
  role    = "roles/composer.worker"
  member  = "serviceAccount:${google_service_account.sa_composer.email}"
}

# # Attach role ServiceAgentV2Ext in service account composer
# resource "google_project_iam_member" "attach_role_composer-agentv2" {
#   project = var.project_id
#   role    = "roles/composer.ServiceAgentV2Ext"
  
#   member  = "serviceAccount:${google_service_account.sa_composer.email}"
# }

# Create composer instance
resource "google_composer_environment" "cluster_config_composer" {
  project = var.project_id
  name   = var.composer_name
  region = var.region
  provider = google-beta
  labels = {env = var.work_environ}

  storage_config {
      bucket  = google_storage_bucket.create_bucket.name
    }

  config {

    software_config {
        image_version = var.image_version_composer
        airflow_config_overrides = {
            core-dags_are_paused_at_creation = "True"
            secrets-backend                  =  "airflow.providers.google.cloud.secrets.secret_manager.CloudSecretManagerBackend"
            secrets-backend_kwargs           =  "{'project_id': '${var.project_id}', 'connections_prefix':'airflow-connections', 'variables_prefix':'airflow-variables', 'sep':'-'}"
        }

        env_variables = {
            work_environ = var.work_environ
        }
        # cloud_data_lineage_integration {
        #     enabled  = true
        # }
    }

    workloads_config {
        scheduler {
          cpu        = 1
          memory_gb  = 2
          storage_gb = 2
          count      = 1
        }
        web_server {
          cpu = 1
          memory_gb = 2
          storage_gb = 2
        }

        worker {
            cpu = 1
            memory_gb = 2
            storage_gb = 2
            min_count = 1
            max_count = 3
        }
        triggerer {
            cpu = 0.5
            memory_gb = 0.5
            count = 1
        }

    }
    environment_size = "ENVIRONMENT_SIZE_SMALL"

    # node_config {
    #   network               = "projects/${var.network_project}/global/networks/${var.network_name}"
    #   subnetwork            = "projects/${var.network_project}/regions/${var.region}/subnetworks/${var.subnet_name}"
    #   service_account       = google_service_account.sa_composer.name
    #   ip_allocation_policy {
    #     cluster_secondary_range_name    = var.ip_range_pods
    #     services_secondary_range_name   = var.ip_range_services
    #   }

    # }

    # private_environment_config {
    #   enable_private_endpoint              = false
    #   cloud_composer_connection_subnetwork = "projects/${var.network_project}/regions/${var.region}/subnetworks/${var.subnet_name}"
    # }
  }

}