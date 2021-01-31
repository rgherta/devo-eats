module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google//modules/private-cluster"
  project_id                 = var.project_name
  name                       = "friendly-eats-cluster"
  region                     = var.region
  zones                      = [var.zone]
  network                    = module.network.network_name
  subnetwork                 = "subnet-b"
  ip_range_pods              = "pod-cidr"
  ip_range_services          = "svc-cidr"
  http_load_balancing        = false
  horizontal_pod_autoscaling = true
  network_policy             = true
  enable_private_endpoint    = false
  enable_private_nodes       = true
  master_ipv4_cidr_block     = "172.16.0.0/28"

  node_pools = [
    {
      name               = "default-node-pool"
      machine_type       = "e2-medium"
      min_count          = 1
      max_count          = 1
      disk_size_gb       = 100
      disk_type          = "pd-standard"
      image_type         = "COS"
      auto_repair        = true
      autoscaling        = true
      auto_upgrade       = true
      service_account    = var.service_account
    },
  ]

  node_pools_labels = {
    all = {}
    default-node-pool = {
      default = true
    }
  }

  cluster_resource_labels = {
      env = "test"
  }

}