import json
import base64
import boto3

SCONES_ENDPOINT_NAME = "sconesClassifierModelEndpoint"

runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    response = runtime.invoke_endpoint(
        EndpointName=SCONES_ENDPOINT_NAME,
        ContentType='image/png',
        Body=image)

    result = json.loads(response['Body'].read().decode('utf-8'))

    return {
        'statusCode': 200,
        'body': {
            "inferences": result
        }
    }