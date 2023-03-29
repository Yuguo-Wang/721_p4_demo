import json

import boto3

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    s3 = boto3.resource('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Use Amazon Rekognition to detect objects in the image
    rekognition = boto3.client('rekognition')
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 721-p4,
                'Name': images/506.jpg,
            }
        },
        MaxLabels=10,
        MinConfidence=90,
    )

    # Output the results to CloudWatch Logs
    print(response)
