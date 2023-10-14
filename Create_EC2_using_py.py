import boto3
import yaml
import os

def read_config_from_yaml(file_path):
    
    print(f"Yaml File path trying to reach: {file_path}")
    
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            print(f"Config Loaded: {config}")  # Debugging print
            return config
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error in YAML file: {e}")
        return None

def ec2_demo():
  
    # Read the entire config from the YAML file
  
    config = read_config_from_yaml(r'c:\Users\pc\PGDIP\IaC\EC2-config.yaml')
    
    # Check if the config is loaded correctly
    if config is None:
        print("Configuration is empty, exiting.")
        return

    ec2 = boto3.resource('ec2')
    
    demo_instance = ec2.create_instances(
        ImageId=config['ImageId'],
        MinCount=config['MinCount'],
        MaxCount=config['MaxCount'],
        InstanceType=config['InstanceType'],
        KeyName=config['KeyName'],
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
    print("Created?")
