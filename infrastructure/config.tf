terraform {
  backend "gcs" {
    bucket  = "deployments-dvtm"
    prefix  = "terraform/state/dev"
  }
}

provider "google" {
  project     = var.project_name
  region      = var.region
}