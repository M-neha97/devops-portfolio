

variable "aws_region" {
  description = "The AWS region where resources will be provisioned."
  type        = string
  default     = "ap-south-1"
}

variable "env" {
  description = "value"
  default = "dev"
}

variable "cidr_block" {
  
  default = "10.0.0.0/16"
}
