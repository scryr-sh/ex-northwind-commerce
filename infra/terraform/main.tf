terraform {
  required_version = ">= 1.8.0"
}

variable "environment" {
  type        = string
  description = "Deployment environment name."
}

variable "region" {
  type        = string
  description = "Primary deployment region."
}

variable "web_image" {
  type        = string
  description = "Container image tag for northwind-web."
}

variable "api_image" {
  type        = string
  description = "Container image tag for northwind-api."
}

variable "postgres_size" {
  type        = string
  description = "Managed Postgres size class."
}

variable "redis_size" {
  type        = string
  description = "Managed Redis size class."
}

output "promotion_summary" {
  value = {
    environment   = var.environment
    region        = var.region
    web_image     = var.web_image
    api_image     = var.api_image
    postgres_size = var.postgres_size
    redis_size    = var.redis_size
  }
}
