terraform {
  backend "gcs" {
    bucket  = "personal-terraform-backend"
    prefix  = "state"
  }
 
}