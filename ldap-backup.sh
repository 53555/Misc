#!/bin/bash

DATE=$(date +%Y-%m-%d-%H%M%S)
BACKUP_FILE="backup_$DATE.ldif"

#take backup of ldap
/sbin/slapcat -b "dc=appstack,dc=net" -l $BACKUP_FILE
if [[ $? -eq 0 ]]
then
        echo "LDAP backup created $BACKUP_FILE"
else
        echo "LDAP backup failed"
fi

BUCKET_NAME="ldap-backup-test1"
REGION="us-east-2"
S3_BUCKET_NAME=$(aws s3 ls | grep $BUCKET_NAME|awk -F" " '{print $3}')

if [[ $S3_BUCKET_NAME != $BUCKET_NAME ]]
then
        aws s3 mb s3://$BUCKET_NAME --region $REGION
else
        echo "$BUCKET_NAME already exist"
fi

#upload ldap backup to S3
aws s3 cp $BACKUP_FILE s3://$BUCKET_NAME/

if [[ $? -eq 0 ]]
then
    rm -rf $BACKUP_FILE
else
    echo "Upload to S3 bucket failed"
fi
