# writing trigger file to enriched bucket
trigger_file_text = "This is triger file for next pipeline (Project 4)"
client = boto3.client('s3')
client.put_object(Body=trigger_file_text, Bucket=trg_file_bucket.split("//")[1].split("/")[0], Key='trigger_file.txt')