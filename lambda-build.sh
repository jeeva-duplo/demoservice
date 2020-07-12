#!/bin/bash -ex
cd ~/workspace/demoservice/mysite
sudo rm -rf duplo
. ~/.bashrc
virtualenv duplo
. duplo/bin/activate
#pip install awscli boto click zappa requests  django
pip install zappa
pip install -r requirements.txt
find . -name '*.pyc' -delete
rm -rf *.zip
zappa package dev
aws s3 cp *.zip  s3://$S3_BUCKET_DEMO/
