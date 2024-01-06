from decode_function import BucketReader
from mail_client import MailService


def lambda_handler(event, context):
    bucket_reader = BucketReader()
    mail_sender = MailService()
    address_str = bucket_reader.read_object_content(bucket=event["bucket"], object_key=["address"])
    try:
        content_str = bucket_reader.read_object_content(bucket=event["bucket"], object_key=["content"])
    except Error:
        content_str = 'ceva'
    mail_sender.send_mail(source_address=address_str, destination_address=address_str, content=content_str)

@patch('client.decode_function.BucketReader')
@patch('client.mail_client.MailService')
def test(patch_bucket_reader: MagicMock,
        patch_mail_service: MagicMock):
    bucket_reader = Mock()
    mail_service = Mock()
    patch_bucket_reader.return_value = bucket_reader
    ...
    bucket_reader.read_object_content(bucket='bucket_name', object_key='address').return_value = 'adresa@email.com'
    bucket_reader.read_object_content(bucket='bucket_name', object_key='content_object').side_effect = BucketReaderError('...', exc)
    lambda_handler(event, context)
    mail_sender.assert_called_once_with(source_address= 'adresa@email.com', dest = 'adresa@email.com', content='ceva')


    
