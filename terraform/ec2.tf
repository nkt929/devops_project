resource "aws_instance" "instance" {
  ami             = "ami-00399ec92321828f5"
  instance_type   = "t2.micro"
  security_groups = ["group-1"]
  key_name        = "my_key"
  tags = {
    Name = "Devops"
  }
}
output "my-public-ip" {
  value = aws_instance.instance.public_ip
}
