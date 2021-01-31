variable "project_name" {
  type    = string
  description = "Name of GCP project. Must be created beforehand"
}

variable "service_account" {
  type    = string
  description = "Service account with owner role for project_name"
}

variable "region" {
  type    = string
  description = "Region to provision resources"
}

variable "zone" {
  type    = string
  description = "Zone to provision resources"
}



