module "network" {
  source  = "terraform-google-modules/network/google"
  version = "3.0.1"

  project_id   = var.project_name
  network_name = "vpc-cluster"
  routing_mode = "REGIONAL"

  subnets = [
        {
            subnet_name           = "subnet-a"
            subnet_ip             = "192.168.128.0/28"
            subnet_region         = var.region
            description           = "Public subnet used to host services reacheable from internet"
        },
        {
            subnet_name           = "subnet-b"
            subnet_ip             = "192.168.32.0/22"
            subnet_region         = var.region
            subnet_private_access = "true"
            description           = "Private subnet used for services unreachable from internet"
        }
    ]

    secondary_ranges = {
        subnet-a = []
        subnet-b = [
            {
                range_name    = "pod-cidr"
                ip_cidr_range = "192.168.36.0/23"
            },
            {
                range_name    = "svc-cidr"
                ip_cidr_range = "192.168.39.224/27"
            },
        ]

    }

    routes = [
        {
            name                   = "egress-internet"
            description            = "route through IGW to access internet"
            destination_range      = "0.0.0.0/0"
            tags                   = "egress-inet"
            next_hop_internet      = "true"
        }
    ]

}