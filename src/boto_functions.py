import boto3
from config import config


def instantiate_client(access_key, secret_key, region):
    client = boto3.client(
        "ec2",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region,
    )
    return client


def list_instance_ids(client):
    response = client.describe_instances()
    InstanceIds = {}

    i = 1
    for groups in response["Reservations"]:
        for instance in groups["Instances"]:
            data = {
                "ID": instance["InstanceId"],
                "Type": instance["InstanceType"],
                "State": instance["State"]["Name"],
                "Security Group": instance["SecurityGroups"][0]["GroupName"],
                "Key Name": instance["KeyName"],
                "Private IP Adress": instance["PrivateIpAddress"],
            }

            InstanceIds[f"Instance {i}"] = data
            i += 1
    return InstanceIds
