

# Create a security group to allow SSH access (port 22)
resource "aws_security_group" "nginx-sg-test" {
  name        = "nginx-sg"
  description = "Allow SSH inbound traffic"
  vpc_id = aws_vpc.terraform_test_vpc.id

  tags = {
    Name = "nginx-sg-test"
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

