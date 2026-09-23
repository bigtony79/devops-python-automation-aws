import boto3

ec2_client_east = boto3.client('ec2', region_name='us-east-1')
ec2_resource_east = boto3.resource('ec2', region_name='us-east-1')

instance_ids_east = []


reservations_east = ec2_client_east.describe_instances()['Reservations']
for reservation in reservations_east:
    instances = reservation['Instances']
    for instance in instances:
        instance_ids_east.append(instance['InstanceId'])
    
response = ec2_resource_east.create_tags(
    Resources= instance_ids_east,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)  


