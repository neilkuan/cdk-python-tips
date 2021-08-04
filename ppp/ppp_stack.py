from aws_cdk import (
    core as cdk,
    aws_s3 as s3,
)


class PppStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, bucketname: str or None = None,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # if not defeined, use default bucket name 'defaultbucketname'.
        s3.Bucket(self, 'bucket', bucket_name=bucketname or 'defaultbucketname')
    # stack methods.
    def add_bucket(self, name: str or None = None):
        return s3.Bucket(self, 'bucket'+name, bucket_name=name or 'defaultbucketname')