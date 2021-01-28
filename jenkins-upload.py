#!/usr/bin/python3
import tarfile
import subprocess as sp
import datetime
import os
import boto3

bucket_name = "dev-ldap-jenkins-backup"
backup_file_cmd = "aws s3 ls s3://"+bucket_name+"/| sort -nr | head -1 | awk '{print $4}'"
Jenkins_home = "/var/lib/jenkins/"

backup_file = sp.check_output(backup_file_cmd, shell=True)
backup_file = backup_file.decode("utf-8").split()[0]
print(backup_file)
copy_cmd = "aws s3 cp s3://"+ bucket_name +"/"+ backup_file + " /tmp/"
try:
    upload = sp.check_output(copy_cmd, shell=True)
    print("Upload to /tmp dir successfully")
    with tarfile.open("/tmp/"+backup_file) as TARGZ:
        TARGZ.extractall(path=Jenkins_home)
        TARGZ.close()
    print("Upload completed successfully")
except Exception as e:
    print("upload failed \n" + e)








