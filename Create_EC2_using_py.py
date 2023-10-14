import boto3

def ec2_demo():
    ec2 = boto3.resource('ec2')

    demo_instance = ec2.create_instances(
        ImageId='ami-0bb4c991fa89d4b9b',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='l00157158_key_pair',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'L00157158-EC2-02'},
                    {'Key': 'Environment', 'Value': 'PGDIP-Dev'}
                ]
            }
        ]
    )
    print(demo_instance)

if __name__ == '__main__':
    ec2_demo()
    print("Instance successfully created")
