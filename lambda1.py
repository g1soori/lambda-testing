import json
import boto3
import urllib

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # TODO implement
    
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    copy_source = {
        'Bucket': 'destination-345465',
        'Key': key
    }
    
    s3.meta.client.copy(copy_source, 'source-test-431232', key)

    return {
        'statusCode': 200,
        'body': 'success'
    }
