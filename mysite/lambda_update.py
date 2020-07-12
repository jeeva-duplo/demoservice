#!/usr/bin/env python
import os
import sys
import json
import requests

def update_lambda():
    use_duplo = False
    s3_file = 'apigateway-zappa-demo.zip'
    LAMBDA_NAME = os.getenv('LAMBDA_NAME')
    S3_BUCKET_LAMBDA = os.getenv('S3_BUCKET_LAMBDA')
    TENANTID = os.getenv('TENANTID')

    #available from internal
    if os.getenv('DISCOVERY_EP') is None:
        ## requied from azure devops
        DUPLO_URL = os.getenv('DUPLO_URL')
        API_TOKEN = os.getenv('DUPLO_API_TOKEN')
    if use_duplo :
        use_duplo =True
        DUPLO_URL = os.getenv('DISCOVERY_EP')
        API_TOKEN=""

    #validate
    if LAMBDA_NAME is None:
        print("ERROR: LAMBDA_NAME is requied")
    if S3_BUCKET_LAMBDA is None:
        print("ERROR: S3_BUCKET_LAMBDA is requied")
    if TENANTID is None:
        print("ERROR: TENANTID is requied")
    if DUPLO_URL is None:
        print("ERROR: DUPLO_URL is requied")
    if API_TOKEN is None:
        print("ERROR: API_TOKEN is requied")

    if use_duplo:
        headers = { 'Content-Type': 'application/json' }
    else:
        headers = { "Authorization": "Bearer {0}".format( API_TOKEN ),
                    'Content-Type': 'application/json'  }
    data = {
        "FunctionName": LAMBDA_NAME,
        "Timeout": 20,
        "MemorySize":128,
        "Handler":"handler.lambda_handler",
        "Description":"api gateway demo",
        "Runtime":"python3.7"
    }

    print("")
    print("")
    data = json.dumps(data)
    print("UpdateLambdaFunctionConfiguration start ", data)
    endpoint = "{0}/subscriptions/{1}/UpdateLambdaFunctionConfiguration".format(DUPLO_URL, TENANTID)
    response = requests.post(endpoint, headers=headers , data=data)
    print("UpdateLambdaFunctionConfiguration response ", endpoint, response)
    print("")
    print("")
    #UpdateLambdaFunction
    data = {
     "FunctionName":LAMBDA_NAME,
     "S3Bucket":S3_BUCKET_LAMBDA,
     "S3Key":s3_file
    }
    data = json.dumps(data)
    print("UpdateLambdaFunction start ", data)
    endpoint = "{0}/subscriptions/{1}/UpdateLambdaFunction".format(DUPLO_URL, TENANTID)
    response = requests.post(endpoint, headers=headers , data=data)
    print("UpdateLambdaFunction response ", endpoint, response)

if __name__ == "__main__":
    update_lambda()
