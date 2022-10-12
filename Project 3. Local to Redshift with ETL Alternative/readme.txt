THIS PROJECT IS ABOUT AUTOMATING DATA TRANsFER FROM LOCAL MACHINE TO AWS REDSHIFT DATABASE WHILE IMPLYING ETL STEPS IN BETWEEN
(This project is an alternative, more efficient and less resoursfule version of Project 2.)

There are many ways data pipelines could be developed based on business need and cost optimization prospectives. It intends to demonstrate relationships between different AWS components and may potentially benefit some readers looking to utilize resources covered in this project.

POTENTIAL BUSINESS NEED: Assume a company needs their analytics departments to access sales spreadsheet on daily basis. However, data is generated on several different external locations. Company system on daily basis generates the dataset into specific folder in each local machine per location. Company needs a data pipeline built that once data is exported into said folder would trigger and load datasets onto cloud server, process data (clean it, transfom it per business needs) and finally load it onto final location - Redshift database, from where Analytic team's system would conduct analysis. Project 4 will continue with flow from this and previous projects by reading data from Redshift, conducting analysis and building dashboard based on insights derived from data analysis. 

PROJECT PROPOSED SOLUTION: 
1. Create EC2 server, mount local dataset export path in each location's machine to EC2 server
2. Create a script to load datasets into S3 Raw buket and put it on daily schedule
3. Create Lambda function to send email once file is loaded into S3
4. Create glue jobs to Partition data and load it to Enriched Bucket
5. Glue job to process dataset from Enriched bucket and load onto Redshift
6. Redshift cluster
7. Create StepFunction to orcestrate job executions and use EvenBridge to trigger it
7. Appropriate roles gor glue jobs and Lambdas
8. Networking onfigurations: Endpoints, ACL and Security Groups.

Ultimately, query data in Redshift through console or SQL Workbench to validate it

CHECK OUT OTHER PROJECTS ON MY WEB SITE: www.sharif-cloud.com
