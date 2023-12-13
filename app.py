#!/usr/bin/env python3
import os

import aws_cdk as cdk
from dailymail.dailymail_stack import DailymailStackTest


app = cdk.App()
DailymailStackTest(app, "DailymailStackTest")
app.synth()
