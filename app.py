#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_training.aws_training_stack import AwsTrainingStack


app = cdk.App()
AwsTrainingStack(app, "AwsTrainingStack")

app.synth()
