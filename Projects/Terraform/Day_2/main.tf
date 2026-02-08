provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "sample_instance" {
    ami = "ami-019715e0d74f695be"
    instance_type = "t3.micro"
    tags = {
         Name="demo-server"
         Env="Dev"
    }
}
