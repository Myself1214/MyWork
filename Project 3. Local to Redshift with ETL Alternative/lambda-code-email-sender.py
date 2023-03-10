import os
import boto3
import smtplib
import yaml

def lambda_handler(event, context):
    config_bucket = os.environ.get('config_bucket')
    config_file = os.environ.get('config_file')

    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=config_bucket, Key=config_file)
    config_file = yaml.safe_load(obj['Body'].read().decode('utf-8'))

    email_user = config_file['email_user']
    email_password = config_file['email_password']
    send_to = config_file['send_to']

    
    raw_bucket = os.environ.get('raw_bucket')
    raw_file_folder = os.environ.get('raw_trigger_folder')
    s3 = boto3.resource("s3")
    s3_bucket = s3.Bucket(raw_bucket)
    files_in_s3 = [f.key.split(raw_file_folder + "/")[1] for f in s3_bucket.objects.filter(Prefix=raw_file_folder).all()]
    raw_file = files_in_s3[1]
    
    subject = 'NEW FILE UPLOADED TO YOUR S3 RAW BUCKET'
    body = f'A new file named "{raw_file}" was uploaded into your raw S3 bucket: "{raw_bucket}"'
    email_content = f'From: {email_user}\nTo: {send_to}\nSubject: {subject}\n\n{body}'

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        smtp_server.ehlo()
        smtp_server.login(email_user, email_password)
        smtp_server.sendmail(email_user, send_to, email_content)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)