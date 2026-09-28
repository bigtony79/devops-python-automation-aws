import boto3

ec2_client = boto3.client('ec2')

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod'] #This will filter the volumes to only include those with a Name tag that contains the string "prod"                      
        }
    ])['Volumes']
print(volumes)

for volume in volumes:
   snapshots = ec2_client.describe_snapshots(
       OwnerIds=['self'], #This will filter the snapshots to only include those owned by your AWS account
       Filters=[
           {
               'Name': 'volume-id',
               'Values': [volume['VolumeId']] #This will filter the snapshots to only include those associated with the current volume
           }
       ]
   )['Snapshots']
   
   print("Unsorted list of snapshots:")
   for snapshot in snapshots:
       snapshot_id = snapshot['SnapshotId']
       snapshot_volume_id = snapshot['VolumeId']
       snapshot_state = snapshot['State']
       snapshot_start_time = snapshot['StartTime']
       print(f"Snapshot ID: {snapshot_id} - Volume ID: {snapshot_volume_id} - State: {snapshot_state} - Start Time: {snapshot_start_time}")    
       print("##########################################################################")

   sorted_snapshots = sorted(snapshots, key=lambda x: x['StartTime'], reverse=True) # Sort the snapshots by StartTime in descending order. Lambda function is used to extract the StartTime from each snapshot dictionary for sorting.

   print("Sorted Snapshots by Start Time (Most Recent First):")
   for snapshot in sorted_snapshots:
       snapshot_id = snapshot['SnapshotId']
       snapshot_volume_id = snapshot['VolumeId']
       snapshot_state = snapshot['State']
       snapshot_start_time = snapshot['StartTime']
       print(f"Snapshot ID: {snapshot_id} - Volume ID: {snapshot_volume_id} - State: {snapshot_state} - Start Time: {snapshot_start_time}")
       print("##########################################################################")

   print("Deleting older snapshots, keeping only the most recent 2 snapshots for each volume...")
   for snapshot in sorted_snapshots[2:]: # Skip the first 2 snapshots (most recent) and delete the rest
       snapshot_id = snapshot['SnapshotId']
       snapshot_volume_id = snapshot['VolumeId']
       print(f"Deleting Snapshot ID: {snapshot_id} for Volume ID: {snapshot_volume_id}")
       delete_snapshot_response = ec2_client.delete_snapshot(
       SnapshotId= snapshot_id    
       )
       print(delete_snapshot_response)
   
  
