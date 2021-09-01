resource "null_resource" "remote" {
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("../my_key.pem")
    host        = aws_instance.instance.public_ip
  }
  provisioner "remote-exec" {
    inline = [
      "cd /var/www/html/web/",
      "echo 'HelloWorld' > index.html",
      "nohup busybox httpd -f -p 8080 &",
    ]
    on_failure = continue
  }
}
