$awsProfile="fcc-dev"               # make sure you are adding your configured profile name as variable for awsprofile
$awsRegion="eu-central-1"           # make sure you are adding correct region where your stepfunction available 
$awsAccount="123456789098"          # add correct aws account number
$stepFunctionName="staging-DatabaseBackupHA" # add stepfunction name

$executionList = aws stepfunctions list-executions --state-machine "arn:aws:states:${awsRegion}:${awsAccount}:stateMachine:${stepFunctionName}" --status-filter "RUNNING" --profile $awsProfile --region $awsRegion --query "executions[].executionArn" --output json | ConvertFrom-Json

$executionList >> SFExecutionsARN.txt

foreach($execution in $executionList){
    Write-Host $execution
    aws stepfunctions stop-execution --execution-arn $execution --region $awsRegion --profile $awsProfile