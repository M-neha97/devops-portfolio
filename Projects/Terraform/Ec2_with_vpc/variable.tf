variable "instance_type" {
  type        = string
  description = "EC2 instance type for the web server"
  default     = "t3.micro"
}

variable "aws_region" {
  description = "The AWS region where resources will be provisioned."
  type        = string
  default     = "ap-south-1"
}

variable "availability_zone" {
    type = string
    default = "ap-south-1a"
  
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

variable "ami_ids" {
  description = "A map of AMI IDs per region"
  type        = string
  default = "ami-087d1c9a513324697"
    
}

variable "key_name" {
    description ="key pair to connect to ec2 instance"
    type = string
    default = "terraform-test-key"
  
}
variable "instance_count" {
  description = "Number of instances to provision."
  type        = number
  default = 1
}

variable "volume_size" {
  description = "volume size of ec2"
  type = number
  default = 10
}
