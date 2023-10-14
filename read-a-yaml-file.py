
import boto3
import yaml
import os

file_path = r'c:\Users\pc\PGDIP\IaC\EC2-config.yaml'

def read_config_from_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml_content = file.read()
            print(f"YAML Content: {yaml_content}")
            config = yaml.safe_load(yaml_content)
            print(f"Config Loaded: {config}")
            return config
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error in YAML file: {e}")
        return None
