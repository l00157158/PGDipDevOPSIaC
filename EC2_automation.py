import boto3
import yaml

def read_config_from_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error in YAML file: {e}")
        return None

def create_security_group(ec2_client, name, description):
    response = ec2_client.create_security_group(GroupName=name,
                                               Description=description)
    security_group_id = response['GroupId']

    # Allow inbound SSH
    ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])

    return security_group_id

def ec2_demo():
    config = read_config_from_yaml(r'c:\Users\pc\PGDIP\IaC\EC2-automation.yaml')
    
    if config is None:
        print("Configuration is empty, exiting.")
        return

    ec2 = boto3.resource('ec2')
    ec2_client = boto3.client('ec2')

    # Create a security group to allow SSH traffic
    security_group_id = create_security_group(ec2_client, 'ssh-access', 'Security group to allow SSH traffic')

    # Create EC2 instance
    demo_instance = ec2.create_instances(
        ImageId=config['ImageId'],
        MinCount=config['MinCount'],
        MaxCount=config['MaxCount'],
        InstanceType=config['InstanceType'],
        KeyName=config['KeyName'],
        SecurityGroupIds=[security_group_id],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': config['Tags']
            }
        ]
    )
    print(demo_instance)

if __name__ == '__main__':
    ec2_demo()
