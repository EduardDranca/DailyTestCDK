import boto3
ses = boto3.client('ses')


def handler(event, context):
    content = event["detail"]["content"][0]
    address = event["detail"]["address"][0]
    source = event["detail"]["address"][0]
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

