import boto3
import schedule

ec2_client = boto3.client('ec2')

def create_ec2_volume_snapshot():
    volumes = ec2_client.describe_volumes()['Volumes']
    for volume in volumes:
        print(f"Volume ID: {volume['VolumeId']} and Instance ID: {volume['Attachments'][0]['InstanceId']}")
        new_snapshot = ec2_client.create_snapshot(       
            VolumeId=volume['VolumeId']    
        )
        print(new_snapshot)

schedule.every(1).minutes.do(create_ec2_volume_snapshot)

while True:
    schedule.run_pending()