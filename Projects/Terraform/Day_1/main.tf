// creating an ec2 instance 

provider "aws" {
    region = "ap-south-1"
  
}

resource "aws_instance" "instance_creation" {
    ami = "ami-019715e0d74f695be"
    instance_type = "t3.micro"
    tags = {
         Name="demo-server"
         Env="Dev"
    }
    
}

output "public_ip" {
    description = "Public Ip address"
    value = aws_instance.instance_creation.public_ip  
}
