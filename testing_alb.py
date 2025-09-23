import os
import boto3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Create a session with explicit credentials
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),  # optional
    region_name=os.getenv('AWS_REGION', 'us-east-2')
)

client = session.client('elbv2')
def list_all_albs():
    try:
        response = client.describe_load_balancers()
        
        if not response['LoadBalancers']:
            print("No load balancers found.")
            return []
        
        print("Found Load Balancers:")
        print("-" * 50)
        
        alb_names = []
        for lb in response['LoadBalancers']:
            lb_name = lb['LoadBalancerName']
            lb_type = lb['Type']
            lb_scheme = lb['Scheme']
            lb_state = lb['State']['Code']
            lb_dns = lb['DNSName']
            
            print(f"Name: {lb_name}")
            print(f"Type: {lb_type}")
            print(f"Scheme: {lb_scheme}")
            print(f"State: {lb_state}")
            print(f"DNS: {lb_dns}")
            print("-" * 50)
            
            alb_names.append(lb_name)
        
        return alb_names
        
    except Exception as e:
        print(f"Error listing load balancers: {e}")
        return []

def alb_exists(alb_name):
    try:
        res = client.describe_load_balancers(Names=[alb_name])
        print(res)
        return True
    except client.exceptions.LoadBalancerNotFound as ex:
        print(f"ALB {alb_name} not found.")
        return False
    
alb_exists("my-alb")