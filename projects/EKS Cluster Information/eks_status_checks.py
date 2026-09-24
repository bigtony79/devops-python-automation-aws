import boto3

eks_client = boto3.client('eks')
clusters = eks_client.list_clusters()['clusters']

for cluster in clusters:
    response = eks_client.describe_cluster(
    name=cluster
    )
    cluster_info = response['cluster']
    cluster_version = cluster_info['version']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    print(f"Version of {cluster}: {cluster_version}")
    print(f"Status of {cluster}: {cluster_status}")
    print(f"Endpoint of {cluster}: {cluster_endpoint}")




