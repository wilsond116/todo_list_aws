import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoList')


def lambda_handler(event, context):
    http_method = event['httpMethod']

    if http_method == 'GET':
        try:
            response = table.scan()
            return {
                'statusCode': 200,
                'body': json.dumps(response['Items'])
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

    elif http_method == 'POST':
        try:
            data = json.loads(event['body'])
            if 'task' not in data:
                raise ValueError("Task is required")
            todo_id = str(uuid.uuid4())
            table.put_item(Item={'id': todo_id, 'task': data['task'], 'completed': False})
            return {
                'statusCode': 201,
                'body': json.dumps({'id': todo_id, 'task': data['task'], 'completed': False})
            }
        except Exception as e:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': str(e)})
            }

    elif http_method == 'DELETE':
        if 'queryStringParameters' not in event or 'id' not in event['queryStringParameters']:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing id parameter'})
            }
        todo_id = event['queryStringParameters']['id']
        try:
            table.delete_item(Key={'id': todo_id})
            return {
                'statusCode': 204,
                'body': json.dumps({'message': 'Item deleted successfully'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }
