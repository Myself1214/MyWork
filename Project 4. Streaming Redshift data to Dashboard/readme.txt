LIVE DATA STREAM WITH KINESIS FROM REDSHIFT AND DELIVERY TO QUICKSIGHT DASHBOARD

This project is aimed to design an AWS cloud based data pipeline that will:
- read a table from redshift database
- simulate streaming data delivery into S3 bucket
- crawlers will read the data from S3 bucket and create metadata table called -  catalog
- quicksight dashboard will pick up streaming data from data catalog though direct athena queries when an update is performed

Following AWS services are utilized in this project:
- Simple Storage Service - S3
- AWS Systems Manager
- IAM
- Lambda Function
- Glue Crawler
- Amazon EventBridge Service
- EC2
- Kinesis Data Stream Service
- Kinesis Firehose Delivery Service
- QuickSight Service - Dahsboard
- Athena Service

Other tools and technoliogies:
- Python
- WS PowerSell
- Command Prompt
- JSON
- AWS CDK

Check out other projects at: www.sharif-cloud.com
