AWS Security Function Automation Project by Jake and Miranda
<p> In this project, we create a mock system for a hospital. We created a VPC for the hospital with a public and private subnet. The system includes public EC2 instances for each department, a bastion server to allow the public instances access to the database, and a private database server. Within the database server, we have a MySQL database that contains two tables: medical data and billing data. Each department has a log in to the database and each department has different levels of accessibility to each table depending on their role. This multilayered security approach helps heavily protecy our sensitive data. The essence of our project is automating security alerts using AWS lambda. We created a lambda function that sends security alerts to the IT department upon multiple failed attempts into our bastion server. This allows us to protect our sensitive data against brute force attacks. 
  We use AWS resources and infastructure to automate encyrption for users on the organization's platform as well as authomate security alerts upon suspicious activity.</p>



