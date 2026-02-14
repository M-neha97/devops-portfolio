

provider "aws" {
 region  = var.aws_region # Or the region specified in your profile
 
}



resource "aws_instance" "createinstance" {
  ami           = var.ami_ids  #europe region
  instance_type = var.instance_type
  key_name = var.key_name
  #security_groups = [aws_security_group.nginx-sg-test.name]
  
  vpc_security_group_ids = [aws_security_group.nginx-sg-test.id]
  subnet_id = aws_subnet.public_subnet.id

  #security_groups = [aws_security_group.ssh_security_group.name]
  associate_public_ip_address = true
  # Configure the root EBS volume
  root_block_device {
    volume_size = var.volume_size      # Sets the storage size to 10 GB
    volume_type = "gp3"   # General Purpose SSD (gp3) is generally recommended
  }

  tags = {
    Name = "Dev-nginx-server" 
  }
  
#to connect to Ec2 instance
connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("keyname.pem")
    host        = self.public_ip
    port = 22
  }

# Upload user_data.sh script to EC2 instance after creation 
provisioner "file" {
    
    source="user_data.sh"
    destination="/home/ubuntu/user_data.sh"
  }
 




}



