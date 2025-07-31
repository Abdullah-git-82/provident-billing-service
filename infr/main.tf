# main.tf
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.11.0"
    }
  }
}

provider "kubernetes" {
  config_path    = "~/.kube/config" # Points to Docker Desktop's Kube config
  config_context = "docker-desktop"
}

resource "kubernetes_namespace" "billing_ns" {
  metadata {
    name = "billing"
  }
}