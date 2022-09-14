import sys
import json
import boto3
import pandas as pd
import dask.dataframe as da
from awsglue.utils import getResolvedOptions
import yaml

#================Readig file from s3, repartitioning it and saving in .parquet format in another bucket=================

# Extrating job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME','config_bucket','config_file'])

# Assigning config file to a variable 'config_file'
bucket = args['config_bucket']
conf_file = args['config_file']
s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket, Key=conf_file)
config_file = yaml.safe_load(obj['Body'].read().decode('utf-8'))

# retrieving config file elements into seperate variables
source_file_bucket = config_file['source_file_bucket']
file_path = config_file['file_path']


    #===============Reading file from s3 bucket===========================
s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')
obj = s3.get_object(Bucket= source_file_bucket, Key= file_path) 
# get object and file (key) from bucket

df = pd.read_csv(obj['Body'], skipinitialspace = True) # 'Body' is a key word

# =============Partitioning data into 6 parts and saving it in another bucket in parquet format====================
ddf = da.from_pandas(df, npartitions=6)

#cleaniing old files in s3
s3_resource.Object('sharif-bucket2', '*').delete()

#writing partitions in parquet format
object = s3_resource.Object('sharif-bucket2', '_metadata')
object.put(Body=(bytes(json.dumps(ddf.to_parquet('s3://sharif-bucket2'), default=str).encode())))