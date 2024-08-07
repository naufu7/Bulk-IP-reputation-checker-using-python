This python script iterate given IP's through the RBL checkers. Usually, we are using MXtoolbox to determine the reputation of the IP. However, if you wants to check the reputation for more than 50 IP's per day, MX toolbox should ban your IP and needs to go for premium plan for the process. This code help to list out the reputation of n number of IP's under a file and give us the result if the IP is okay or not. 


> This codes works on python3

> apt-get install -y python3-pip   # Need to install pip3

> pip3 install dnspython==1.15.0   # Need to install this module for dns resolver. 
