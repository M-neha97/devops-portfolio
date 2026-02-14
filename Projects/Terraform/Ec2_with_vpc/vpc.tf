

# 1. Create a VPC
resource "aws_vpc" "terraform_test_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true # Recommended for public subnets
  tags = {
    Name = "terraform-vpc-test"
  }
}

# 2. Create an Internet Gateway (IGW) and attach it to the VPC
resource "aws_internet_gateway" "test_igw" {
  #vpc_id = aws_vpc.example_vpc.id
  vpc_id = aws_vpc.terraform_test_vpc.id
  tags = {
    Name = "terraform-test-igw"
  }
}

#  Create a public subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.terraform_test_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = var.availability_zone
  # Enable auto-assigning public IPs to instances launched in this subnet
  map_public_ip_on_launch = true 
  tags = {
    Name = "Terraform-Test-public-subnet"
  }
}

# 4. Create a Custom Route Table
resource "aws_route_table" "test_public_rtb" {
  #vpc_id = aws_vpc.example_vpc.id
  vpc_id = aws_vpc.terraform_test_vpc.id
  
  tags = {
    Name = "test_public_rtb"
  }
}

# 5. Add a route to the Internet Gateway in the route table
resource "aws_route" "internet_access_route" {
  route_table_id         = aws_route_table.test_public_rtb.id
  destination_cidr_block = "0.0.0.0/0"      # Destination for all internet traffic
  gateway_id             = aws_internet_gateway.test_igw.id
}

# 6. Associate the Route Table with the Public Subnet
resource "aws_route_table_association" "example_public_subnet_assoc" {
 # subnet_id      = aws_subnet.example_public_subnet.id
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.test_public_rtb.id
}
