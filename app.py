#!/usr/bin/env python3

from aws_cdk import core

from my_first_s3_app.my_first_s3_app_stack import MyFirstS3AppStack


app = core.App()
MyFirstS3AppStack(app, "my-first-s3-app")

app.synth()
