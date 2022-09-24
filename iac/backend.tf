terraform {
  backend "s3" {
    bucket = "apigw-tfstate"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}
