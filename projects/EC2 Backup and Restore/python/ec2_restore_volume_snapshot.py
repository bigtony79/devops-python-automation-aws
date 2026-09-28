import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

instance_id ='i-0c30fccd9e9bf46ca' # Replace with your instance ID

# Get volumes attached to the instance
volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
       ]
    )['Volumes']

instance_volume = volumes[0]

# Get all snapshots for volume attached to desired instance
snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'], #This will filter the snapshots to only include those owned by your AWS account
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        }
    ]
)

latest_snapshots = sorted(snapshots['Snapshots'], key=lambda x: x['StartTime'], reverse=True) # Sort the snapshots by StartTime in descending order. Lambda function is used to extract the StartTime from each snapshot dictionary for sorting.

# Create a new volume from the latest snapshot
new_volume = ec2_client.create_volume(
    SnapshotId=latest_snapshots[0]['SnapshotId'],
    AvailabilityZone=instance_volume['AvailabilityZone'],
    VolumeType=instance_volume['VolumeType'],
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instance_volume['Tags'][0]['Value'] + '-restored' # Append '-restored' to the original volume name
                }
            ]
        }
    ]
)

# Attach new volume to desired instance
while True:
   vol = ec2_resource.Volume(new_volume['VolumeId'])
   print(vol.state)
   if vol.state == 'available':
    print("New Volume is available!")
    ec2_resource.Instance(instance_id).attach_volume(
        VolumeId = new_volume['VolumeId'],
        Device = '/dev/xvdb'
    )
    break
   
   
   
   
   
   