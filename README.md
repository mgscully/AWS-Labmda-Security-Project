#AWS Security Function Automation Project by Jake and Miranda

##Summary
<p> This project uses AWS lambda and cloudwatch to automate security alerts and measures for a sample hospital web environment. We specifically aim to prevent and respond to brute force ssh attacks. </p>

##Features 
-EC2 instance monitoring: monitors invalid ssh attempts bastion host using cloudwatch 
-Emails notification via AWS SNS: IT administrator receives email upon detection of 2 or more invalid ssh attempts 
-Bastion host termination upon suspicious ssh attempts 
-Full team notification via slack 

##Requirements 
-AWS 
-Slack webhook 
-Python 3 environment

##Setup 
-Upload lambda function to AWS management console 
-Change url in function to your slack webhook
-Ensure IAM role associated with lambda functions has permisions to stop EC2 instances and send logs to cloudwatch 
-Create cloudwatch alarm that monitors ssh attempts on /var/log/secure 
-Set the alarm to trigger after 2 or more invalid attempts within a certain timeframe 




