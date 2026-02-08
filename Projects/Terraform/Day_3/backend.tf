terraform {
    backend "s3" {

        bucket = "terraform-s3-demo-backend"
        key = "Terraform/terraform.tfstate"
        region = "ap-south-1"   
    }
}
