'''Porivision/Terminate instance'''

import boto3
from flask import Flask

app = Flask(__name__)

class Instance:
    def __init__(self, states, ami_id, instance_type, key_name):
        self.instances = []
        self.states = states

    def init_boto_client(self):
        self.ec2 = boto3.client('ec2')
        return True

    def provision(self):
        self.id = self.ec2.run_instances(ImageId=self.ami_id,
                               InstanceType=self.instance_type,
                               KeyName=self.key_name,
                               MinCount=1,
                               MaxCount=1)
        print(self.id)

    def terminate(self):
        pass

    def block(self):
        pass

    def allow(self):
        pass


def main():
    states = ['running', 'pending']

    instance = Instance(states, 'ami-0d5d9d301c853a04a', 't2.micro', 'Linux_Laptop')
    print(instance.init_boto_client())

    app.run()


if __name__ == '__main__':
    main()
