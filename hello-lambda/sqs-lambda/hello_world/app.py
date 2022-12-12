import json
import os
import boto3
import logging

import psycopg2
import pymysql

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
    """
    
    _params = event['msg_id']
    msg_body = json.dumps(_params)
    msg = send_sqs_message(os.environ['SQS_QUEUE'], msg_body)

def send_sqs_message(sqs_queue_url, msg_body):
    # Send SQS msessage
    sqs_client = boto3.client('sqs')
    
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url, MessageBody=msg_body, MessageGroupId='1')
        
    except ClientError as e:
        logging.error(e)
        return None
        
    # return : Dictionary containg information about the send message. If error, return None
    return msg

def get_connection():
    connection = pymysql.connect(host=os.environ['MYSQL_ADDR'],
                                 user=os.environ['MYSQL_HOST'],
                                 password=os.environ['MYSQL_PWD'],
                                 db=os.environ['MYSQL_NAME'],
                                 charset='utf8mb4',
                                 autocommit=True,
                                 cursorClass=pymysql.cursors.DictCursor)
                                 
    return connection