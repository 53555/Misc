#!/bin/bash

HOSTNAME=$(hostname -f)

JAR_URL="http://${HOSTNAME}:8080/jnlpJars/jenkins-cli.jar"

TEMP="/tmp"

wget $JAR_URL -P $TEMP/

#Reload configuration of jenkins for HA

/usr/bin/java -jar $TEMP/jenkins-cli.jar -s http://${HOSTNAME}:8080/ -auth jadmin:jadmin reload-configuration

if [[ $? -eq 0 ]]
then
    echo "Reload successfully processed"
else
    echo "Reload failed"
fi