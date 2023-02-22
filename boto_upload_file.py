from botocore.exceptions import ClientError
import logging
import boto3
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    mfa_otp = input("Enter the MFA code: ")

    mfa_otp = mfa_otp

    client = boto3.client('sts')

    mfa_creds = client.get_session_token(
        DurationSeconds=36000,
        SerialNumber='arn:aws:iam::568049784084:mfa/KevinVanDerGugten',
        TokenCode=mfa_otp
    )

    print(mfa_creds['Credentials']['SessionToken'])

    # Upload the file
    s3_client = boto3.client('s3',
                             aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                             aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                             region_name='eu-west-1',
                             aws_session_token=mfa_creds['Credentials']['SessionToken'])

    print(boto3.client('sts').get_caller_identity())

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
