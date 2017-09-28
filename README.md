This python script iterate given IP's through the respective RBL's. Usually, we are using MXtoolbox to determine the reputation of the IP. However, if you wants to check the reputation for more than 50 IP's per day, MX toolbox should block your IP and needs to go for premium plan for the process.


> This codes works on python3

> apt-get install -y python3-pip   # Need to install pip3

> pip3 install dnspython==1.15.0   # Need to install this module for dns resolver. 
