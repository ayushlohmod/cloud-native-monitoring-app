import boto3
ecr_client = boto3.client('ecr')

repository_name = "my-cloud-native-repo"
response = ecr_client.create_respository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)