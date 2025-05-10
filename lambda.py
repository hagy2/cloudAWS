 import json
          import boto3

          dynamodb = boto3.resource('dynamodb')
          table = dynamodb.Table('Orders')

          def lambda_handler(event, context):
              for record in event['Records']:
                  try:
                      body = json.loads(record['body'])
                      print(f"Received outer body: {body}")

                      if 'Message' in body:
                          payload = json.loads(body['Message'])
                      else:
                          payload = body

                      print(f"Processed payload: {payload}")

                      table.put_item(Item=payload)

                  except Exception as e:
                      print(f"Error processing record: {str(e)}")
                      raise e

              return {'statusCode': 200, 'body': 'Order processed successfully'}

