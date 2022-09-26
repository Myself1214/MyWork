THIS PROJECT IS ABOUT AUTOMATING DATA TRANFER FROM LOCAL MACHINE TO AWS REDSHIFT DATABASE WHILE IMPLYING ETL STEPS IN BETWEEN

There are many ways data pipelines could be developed based on business need and cost optimization prospectives. However, this project, while is NOT the best solution to the proposed goal, it intends to demonstrate relationships between different AWS components and may potentially benefit some readers looking to how utilize resources covered in this project. In Project 3, we will build exact same pipeline, however using different AWS resources and compare the results between both pipelines based on speed, agility, sustainability, fault tollerance, cost and other mesuarments of efectiveness.

POTENTIAL BUSINESS NEED: Assume a company needs their analytics departments to access sales spreadsheet on daily basis. However, data is generated on several different external locations. Company system on daily basis generates the dataset into specific folder in each local machine per location. Company needs a data pipeline built that once data is exported into said folder would trigger and load datasets onto cloud server, process data (clean it, transfom it per business needs) and finally load it onto final location - Redshift database, from where Analytic team's system would conduct analysis.

PROJECT PROPOSED SOLUTION: 
1. Create EC2 server, mount local dataset export path in each location's machine to EC2 server
2. Create a script to load datasets into S3 Raw buket and put it on daily schedule
3. Create glue jobs to Partition data and load it to Enriched Bucket
4. SNS to notify users when data gets loaded into Raw bucket and use SNS-SQS-Lambda to trigger glue job
5. Glue job to process dataset from Enriched bucket and load onto Redshift
6. Redshift cluster
7. Appropriate roles gor glue jobs and Lambdas
8. Networking onfigurations: Endpoints, ACL and Security Groups.

Ultimately, query data in Redshift through console or SQL Workbench to validate it

CHECK OUT OTHER PROJECTS ON MY WEB SITE: www.sharif-cloud.com
