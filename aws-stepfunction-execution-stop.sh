#!/bin/bash
awsProfile="efx-prod"                # make sure you are adding your configured profile name as variable for awsprofile
awsRegion="us-west-2"                # make sure you are adding correct region where your stepfunction available 
awsAccount="123456789"               # add correct aws account number
stepFunctionName="prod-DatabaseBackupHA"    # add stepfunction name

executionList=$(aws stepfunctions list-executions --state-machine "arn:aws:states:${awsRegion}:${awsAccount}:stateMachine:${stepFunctionName}" --status-filter "RUNNING" --profile $awsProfile --region $awsRegion --query "executions[].executionArn" --output json | grep "executionArn" | awk -F" " '{print $2}' | awk -F"," '{print $1}')

echo $executionList > SFExecutionsARN.txt

for execution in $executionList
do
    aws stepfunctions stop-execution --execution-arn $execution --region $awsRegion --profile $awsProfile
done