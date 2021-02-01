# Infrastrucutre provisioning with Terraform

## Prerequisites

Step1: Create a project

Step2: Enable GKE api in your project, also GCR

Step3: Create a bucket for storing the tfstate

Step4: Create a service-account with owner role for the current project. 

Save the key in ./keys/service-account.key

Set the environment variable

`export GOOGLE_APPLICATION_CREDENTIALS=./keys/service-account.key`

## Provisioning

Update terraform.tfvars based on prerequisites

Make sure CIDRs in network.tf do not overlap with any existing subnets/vpcs

Step5: Provision
`terraformm init`
`terraform plan`
`terraform apply`

## Administration

The module provisions a network with 2 subnets and a private GKE
Both private and public endpoints are enabled to avoid kubectl jumphost issues.

