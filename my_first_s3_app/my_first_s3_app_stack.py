from aws_cdk import (
    aws_s3 as _s3,
    aws_iam as _iam,
    core
)


class MyFirstS3AppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        bucket=_s3.Bucket(self, "Mybucketid",versioned=True
                          ,encryption=_s3.BucketEncryption.KMS_MANAGED)
        bucket.s3_url_for_object(key=None)
        # The code that defines your stack goes here

        output=core.CfnOutput(
            self,
            "MyBucketOutput",
            value=bucket.bucket_name,
            description="My first cdk Bucket",
            export_name="MyBucketOutput"
            )

        _iam.Group(self,"gid")