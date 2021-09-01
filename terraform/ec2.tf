resource "aws_instance" "instance" {
  ami             = "ami-0ff338189efb7ed37"
  instance_type   = "t3.micro"
  security_groups = ["group-1"]
  key_name        = "my_key"
  tags = {
    Name = "Devops"
  }
}
output "my-public-ip" {
  value = aws_instance.instance.public_ip
}
