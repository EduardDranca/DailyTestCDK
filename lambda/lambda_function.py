import boto3
ses = boto3.client('ses')


def lambda_handler(event, context):
    content = event["content"]
    address = event["address"]
    source = event["address"]
    mail = ses.send_email(Destination={
        'ToAddresses': [address]
    },
        Message={

            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': content,
                }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Test email',
            },
        },
        Source=source
    )
