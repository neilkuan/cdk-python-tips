#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from aws_cdk import core
from ppp.ppp_stack import PppStack


app = core.App()
PppStack(app, "PppStack", bucketname='namebucket')
ppp = PppStack(app, "PppStac2")
# add new bucket to PppStac2 stack named aaa.
ppp.add_bucket(name='aaa')
app.synth()
