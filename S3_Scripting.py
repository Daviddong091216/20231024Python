import boto3
s3= boto3.resource('s3')
bucket_name='daviddong20231024'
try:
    response=s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
    print(response)
except Exception as error:
    print(error)