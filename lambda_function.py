import json
import boto3
import http.client
import os 

def lambda_handler(event, context):
    # Initialize ec2 client 
    ec2 = boto3.client('ec2')
    
    # Find instance ID of bastion host 
    instance_id = event['detail']['instance-id']
        
    # Stop the bastion host 
    ec2.stop_instances(InstanceIds=[instance_id])
        
    # Send Slack notification 
    conn = http.client.HTTPSConnection("hooks.slack.com")
    url = "/services/T07JRGQ7MHR/B07K4CC87DF/0fMgr6N9fyomJnBuCoTZ9AYI"
    message = {
        "text": "Security Alert: An ssh attempt has indicated this system has been compromised. The system has been shut down until the source of the compromise can be identified and remedial measure can be implemented. Please switch to backed up records until the system can go back online."
    }

    #response from http client
    headers = {'Content-Type': 'application/json'}
    conn.request("POST", url, body=json.dumps(message), headers=headers)
    response = conn.getresponse()

    #return response 
    return {
        'statusCode': response.status,
        'body': response.read().decode()
    }
