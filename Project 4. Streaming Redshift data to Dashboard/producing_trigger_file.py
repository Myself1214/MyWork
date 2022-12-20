# writing trigger file to enriched bucket for next pipeline to start

with open("trigger_file.txt", 'rb') as f:
    s3.upload_fileobj(f, "you_enriched_bucket", "trigger_file.txt")