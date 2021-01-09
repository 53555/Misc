#!/usr/bin/python3
import tarfile
import subprocess as sp
import datetime
import os

IP = os.popen('ip addr').read()
IP = IP.split('\n')[8].split()[1].split('/')[0]
now = datetime.datetime.now()
Format = "%Y%m%d%H%M%S"
DATE = now.strftime(Format)

backup_loc = "/var/lib/jenkins"
tar_file_loc = "/tmp/jenkins_"+DATE+"_"+IP+"_tar.gz"


with tarfile.open(tar_file_loc, "w:gz") as tar:
    tar.add(backup_loc)

bucket_name = "ldap-backup-test1"
cmd = "aws s3 cp " + tar_file_loc + " s3://"+bucket_name+"/"
try:
    result = sp.check_output(cmd, shell=True)
    cond = True
except sp.CalledProcessError as e:
    print(e)
    # to bring the logic in for validation
    cond = False

if cond == True:
    print("Backup Upload completed successfully")
    sp.check_output("rm -rf "+tar_file_loc, shell=True)
else:
    print("Backup upload failed "+ e)





