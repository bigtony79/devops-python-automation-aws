import boto3
import schedule

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

# Describe all available EC2 instances using describe_instances
reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f"Status of Instance {instance['InstanceId']}: {instance['State']['Name']}")


# Check the health status of each instance using describe_instance_status which is much easier to use than describe_instances
def check_ec2_health():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True # This will list all instances, including those that are stopped or terminated
    )
    for status in statuses['InstanceStatuses']:
        inst_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state}, Instance Status: {inst_status}, System Status: {sys_status}")
    print("##########################################################\n")

# Write a scheduled health check using scheduler library to run the health check every 5 minutes
schedule.every(5).seconds.do(check_ec2_health)
#Example of setting a specific time for the health check
#schedule.every().monday.at("09:00").do(check_ec2_health)

while True:
    schedule.run_pending() # This will run the scheduled jobs
