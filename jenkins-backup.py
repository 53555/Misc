#!/usr/bin/python3
import tarfile
import subprocess as sp
import datetime
import os
import boto3

IP = os.popen('ip addr').read()
IP = IP.split('\n')[8].split()[1].split('/')[0]
now = datetime.datetime.now()
Format = "%Y%m%d%H%M%S"
DATE = now.strftime(Format)
region_name = "us-east-2"

backup_loc = "/var/lib/jenkins/"
tar_file_loc = "/tmp/jenkins_"+DATE+"_"+IP+".tar.gz"


with tarfile.open(tar_file_loc, "w:gz") as tar:
    tar.add(backup_loc, arcname=os.path.basename(backup_loc))

#Store the list of available buckets in the LIST

S3 = boto3.client('s3')
lb = S3.list_buckets()
lb = lb['Buckets']
buck = []
for i in lb:
    buck.append(i['Name'])

bucket_name = "dev-ldap-jenkins-backup"

#Check if the required bucket exist, if not create it

if not bucket_name in buck:
    S3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region_name
        }
    )
else:
    pass

#Upload the data into bucket
cmd = "aws s3 cp " + tar_file_loc + " s3://"+bucket_name+"/"
try:
    result = sp.check_output(cmd, shell=True)
    cond = True
except sp.CalledProcessError as e:
    print(e)
    # to bring the logic in for validation
    cond = False


#Delete the file from /tmp if the file upload to S3 bucket succeeded
if cond == True:
    print("Backup Upload completed successfully")
    sp.check_output("rm -rf "+tar_file_loc, shell=True)
else:
    print("Backup upload failed "+ e)





