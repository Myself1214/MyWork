# Importing necesary modules
import sys
from awsglue.utils import getResolvedOptions
from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
import yaml
import boto3

# Extrating job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME','config_bucket','config_file'])

# Assigning config file to a variable 'config_file'
bucket = args['config_bucket']
conf_file = args['config_file']
s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket, Key=conf_file)
config_file = yaml.safe_load(obj['Body'].read().decode('utf-8'))

# Retrieving username, password, url, db_table into seperate variables
user = config_file['user']
password = config_file['password']
url = config_file['url']
db_table = config_file['db_table']
trg_file_bucket = config_file['trg_file_bucket']


# Function to write dataframe to redshift 
def write_to_redshift(df, username, passwd, url_endpoint, db_table_name):
    df.write.format("jdbc") \
    .option("url", url_endpoint) \
    .option("dbtable", db_table_name) \
    .option("user", username) \
    .option("password", passwd) \
    .mode('overwrite').save()


# Creating spark session
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


# Reading parquet files from Enriched bucket into PySpark DataFrame
initial_df = spark.read.format("parquet").load(trg_file_bucket)

# removing null values from DataFrame
initial_df = initial_df.na.drop(how="any")

# Removing duplicate columns and index column from DataFrame
initial_df = initial_df.drop('X','Y','ObjectId','__null_dask_index__')

# converting datetime column's type from string to datetime type in DataFrame
initial_df.select(col("call_timestamp"), to_timestamp(col("call_timestamp"), "MM-dd-yyyy HH mm ss SSS").alias("call_timestamp"))

# Writing processed dataframe into a table in Redshift
write_to_redshift(initial_df, user, password, url, db_table)
