# AWS Security Function Automation Project by Jake and Miranda

## Summary
This project uses AWS Lambda and CloudWatch to automate security alerts and measures for a sample hospital web environment. We specifically aim to prevent and respond to brute force SSH attacks.

## Features
- **EC2 Instance Monitoring:** Monitors invalid SSH attempts on the bastion host using CloudWatch.
- **Email Notification via AWS SNS:** IT administrator receives an email upon detection of 2 or more invalid SSH attempts.
- **Bastion Host Termination:** Terminates the bastion host upon suspicious SSH attempts.
- **Team Notification via Slack:** Sends a full team notification through Slack.

## Requirements
- AWS
- Slack Webhook
- Python 3 Environment

## Setup
- Upload Lambda function to AWS Management Console.
- Change the URL in the function to your Slack webhook.
- Ensure the IAM role associated with Lambda functions has permissions to stop EC2 instances and send logs to CloudWatch.
- Create a CloudWatch alarm that monitors SSH attempts on `/var/log/secure`.
- Set the alarm to trigger after 2 or more invalid attempts within a certain timeframe.


