LIVE DATA STREAM WITH KINESIS FROM REDSHIFT AND DELIVERY TO QUICKSIGHT DASHBOARD

This project is aimed to design an AWS cloud based data pipeline that will read a table from redshift database, simulate streaming data delivery into S3 bucket, from where crawlers will read the data and create metadata table called -  catalog, and finally quicksight dashboard will pick up streaming data from data catalog though direct athena queries when an update is performed.
