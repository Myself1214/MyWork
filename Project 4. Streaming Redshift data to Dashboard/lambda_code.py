import boto3

#create glue client to trigger crawler
client = boto3.client("glue")

def lambda_handler(event, context):
    
    crawler_status = client.get_crawler(Name="your_crawler_name")
    
    crawler_status = crawler_status["Crawler"]["State"]
    
    status_code = 0
    
    while status_code == 0:
    
        if crawler_status == "READY":
            response = client.start_crawler(Name="your_crawler_name")
            print(json.dumps(response, indent=4))
            status_code = 1
        else:
            continue