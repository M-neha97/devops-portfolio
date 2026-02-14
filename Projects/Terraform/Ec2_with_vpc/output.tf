output "public_ip" {
    description = "Public Ip address"
    value = aws_instance.createinstance.public_ip 
}
