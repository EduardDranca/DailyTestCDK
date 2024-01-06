from abc import ABC, abstractmethod
from containers import Container
from dependency_injector.wiring import inject, Provide


class IBucketReader(ABC):
    @abstractmethod
    def read_object_content(self, bucket=object, object_key=str):
        pass


class BucketReader(IBucketReader):
    @inject
    def __init__(self, boto3_client=Provide[Container.s3_client]):
        self.s3 = boto3_client

    def read_object_content(self, bucket=object, object_key=str):
        try:
            bucket_object = self.s3.get_object(Bucket=bucket, Key=object_key)
            object_data = bucket_object['Body'].read()
            object_str = object_data.decode('utf-8')
            return object_str
        except Error as err:
            # raise BucketReaderError('eroare', err)
            return BucketReaderError('eroare', err)

# bucket_reader_test.py
class BucketReaderTestCase(...):
    def test_s3_client_works():
        expected_value = 'blabla'
        s3 = Mock()
        s3.get_object.return_value = {'Body': expected_value}
        bucket_reader = BucketReader(s3)
        actual_value = bucket_reader.read_object_content('bucket', 'obj_key')
        s3.get_object.assert_called_once_with('bucket', 'obj_key')
        assert expected_value == actual_value, '...'
    
    def test_s3_client_throws_exception():
        s3 = Mock()
        bucket_reader = BucketReader(s3)
        expected_raised_exception = Exception('a murit mortu')
        s3.get_object.side_effect = expected_raised_exception
        #
        # with self.assertRaises(BucketReaderError) as context:
        #    bucket_reader.read_object_content('bucket', 'obj_key')
        #    self.assertTrue('eroare' in context.exception)
        #    self.assertTrue(expected_raised_exception in context.exception)
        #
        actual_value = bucket_reader.read_object_content('bucket', 'obj_key')
        assert actual_value.message == 'eroare'
        assert actual_value.initial_exception == expected_raised_exception
    
