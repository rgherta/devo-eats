resource "google_container_registry" "registry" {
  project  = "dvotm-project" #local
  location = "EU"
}
