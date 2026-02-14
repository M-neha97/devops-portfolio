provider "aws" {
  region = var.aws_region
}



# 1. Create a VPC
resource "aws_vpc" "terraform_test_vpc" {
  cidr_block = var.cidr_block
  enable_dns_hostnames = true # Recommended for public subnets
  tags = {
    Name = "terraform-vpc-poc"
  }
}

# Create a security group to allow SSH access (port 22)
resource "aws_security_group" "secuity-group-test" {
  name        = "terraform-sg-poc"
  description = "Allow SSH inbound traffic"
  vpc_id = aws_vpc.terraform_test_vpc.id

/*
  depends_on = [
    aws_vpc.terraform_test_vpc
  ]
*/
  tags = {
    Name = "terraform-sg-poc"
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.allowed_ssh_ip] # Restrict this to your specific IP address for better security
  }

  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [var.http_cidr] # Restrict this to your specific IP address for better security
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

