import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('hourly_ping')
    
    try:
        table.update_item(
            Key={'id': 'hours'},
            UpdateExpression="ADD #val :inc",
            ExpressionAttributeNames={'#val': 'value'},
            ExpressionAttributeValues={':inc': 1},
            ReturnValues="UPDATED_NEW"
        )
        
        response = table.get_item(
            Key={
                'id': 'hours'
            }
        )
        
        if 'Item' in response:
            hours_value = response['Item']['value']
            print(f"Stored hours value: {hours_value}")
        else:
            print("No item found with id 'hours'")
        
        return {
            'statusCode': 200,
            'body': f"This bot has been pinged/visited {hours_value} times since deployment.\n(Pings occur once per hour)"
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': 'An error occurred'
        }
