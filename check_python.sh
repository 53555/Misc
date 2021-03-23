pkg=python3
#which $pkg > /dev/null 2>&1
if rpm -q $pkg
then 
	echo "python3 already installed"	
else
	
    runuser -l ec2-user -c "sudo yum install python3 -y"
fi