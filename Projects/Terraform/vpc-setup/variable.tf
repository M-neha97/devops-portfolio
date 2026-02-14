variable "ami" {
  description = "ami of ec2 instance"
  default = "ami-019715e0d74f695be"
}

variable "instance_type" {
  default = "t3.micro"
}



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

variable "allowed_ssh_ip" {
    description = "allow your public ip to port 22 in security group"
    type = string
    default = "0.0.0.0/0"
  
}

variable "http_cidr" {
    description = "allow this cidr block for http -80 port"
    type = string
    default = "0.0.0.0/0"
}
