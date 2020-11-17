from aws_cdk import (
    aws_s3 as _s3,
    core
)


class MyFirstS3AppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        bucket=_s3.Bucket(self, "Mybucketid")
        bucket.s3_url_for_object(key=None)
        # The code that defines your stack goes here
