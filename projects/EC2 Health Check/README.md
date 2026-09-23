
# Health Check: EC2 Status Checks

## Overview

## Technologies Used
* Python
* Boto3
* AWS
* Terraform

## Project Description
* Create 3 EC2 Instances with Terraform
* Write a Python script that fetches statuses of EC2 Instances and prints to the console
* Extend the Python script to continuously check the status of EC2 Instances in a specific interval

## Pre-requisites

## Steps

### 1. Create and define terraform.tvars file
Define terraform.tvars file before running terraform
```
  vpc_cidr_block = DESIRED_VPC_CIDR_BLOCK
  subnet_cidr_block = SUBNET_CIDR_BLOCK
  avail_zone = AVAIL_ZONE
  env_prefix = DESIRED_PREFIX
  my_ip = IP_ADDRESS 
  instance_type = DESIRED_INSTANCE_TYPE
  public_key_location = PUBLIC_KEY_FILE_LOCATION
  image_name = "al2023-ami-2023*"
```
Make sure that you add terraform.tvars in .gitignore file

### 2. Create the EC2 Instances 
```
  terraform init
  terraform plan
  terraform apply
```
### 3. Run main.py to see the status of 3 newly created EC2 instances
```
  python3 main.py
```
![Alt text](images/Output.png)

### 4. Destroy infrastructure using Terraform
```
  terraform destroy
```





## Learning Outcomes
