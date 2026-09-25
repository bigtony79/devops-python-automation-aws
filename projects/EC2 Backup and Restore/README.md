# EC2 Data Backup and Restore

## Overview

## Technologies used
* Python
* Boto3
* AWS

## Project Description
* Write a Python script that automates creating backups for EC2 Volumes
* Write a Python script that cleans up old EC2 Volume snapshots
* Write a Python script that restores EC2 Volumes

## Pre-requisites

## Steps

# 1. Create AWS infrastructure using Terraform
Using Terraform, we will create 3 EC2 Instances which will have Volume tags set to **'prod', 'QA' and 'dev'**.

Define terraform.tfvars file
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

Initialize Terraform
```
  terraform init
```

Review the execution plan
```
  terraform plan
```

Deploy the infrastructure
```
  terraform apply
```
INSERT SCREENSHOTS showing EC2 instances along with Volumes with their assigned tags

## 2. Create Snapshots from volumes attached to EC2 Instances
Before executing the script **ec2_volume_backup.py**,  you can check for Snapshots from the AWS console. It should be empty.
INSERT screenshot showing empty snapshots
Run the script to create snapshots for all the volumes with a minute interval:
```
  python3 ec2_volume_backup.py
```
Insert screenshot of script output
Now the console should show new snapshots created in minute interval for all attached volumes to the EC2 instances
INSERT Screenshot

For real production use cases, the schedule interval should be set to something much longer than a single minute.

### 3. Remove the oldest Snapshots except for the latest 2 copies for a specific volume
The script **ec2_snapshots_cleanup.py** will retain the latest 2 snapshots of the 'prod' volume and remove the rest
Execute the script
```
  python3 ec2_snapshots_cleanup.py
```
The script will do the following:
1. Filter the volumes list with the tag 'prod'
2. Filter the snapshots list with the volumes assigned with the tag 'prod'
3. Print Unsorted list of snapshots (for demo purpose)
   INSERT SCREENSHOT
5. Sort the snapshots based on the key value 'StartTime' in descending order   
7. Print the sorted the list of snapshots in descending order based on the key value for 'StartTime'
   INSERT SCREENSHOT
9. Delete the oldest snapshots and retain the first 2 snapshots
    INSERT SCREENSHOT

### 4. 


## Learning outcomes
