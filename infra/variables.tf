variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "eu-west-2"
}

variable "project_name" {
  description = "Name used to tag and identify all resources for this project"
  type        = string
  default     = "ci-cd-pipeline-aws"
}

variable "ecr_repository_url" {
  description = "ECR repository URL to pull the app image from"
  type        = string
  default     = "365646128279.dkr.ecr.eu-west-2.amazonaws.com/ci-cd-pipeline-aws"
}

variable "image_tag" {
  description = "Docker image tag to deploy"
  type        = string
  default     = "00a63ff907953ea226b1865ae66f7a54309d9f92"
}

variable "container_port" {
  description = "Port the FastAPI app listens on inside the container"
  type        = number
  default     = 8000
}

variable "db_username" {
  description = "Master username for the RDS Postgres instance"
  type        = string
  default     = "appadmin"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "tasks"
}

variable "db_instance_class" {
  description = "RDS instance size"
  type        = string
  default     = "db.t3.micro"
}
