# writing trigger file to enriched bucket for next pipeline to start

with open("trigger_file.txt", 'rb') as f:
    s3.upload_fileobj(f, "sharif-bucket2", "trigger_file.txt")