#!/bin/python3
import requests
import xml.etree.ElementTree as ET


#Update the IP list in intel IP list 
#response=requests.get("""https://172.16.16.16:4444/webconsole/APIController?reqxml=<Request><Login><Username>adminapi</Username>
#<Password>Password</Password></Login><Set operation="update"><IPHost><Name>Threat-intel-IPs</Name>
#<IPFamily>IPv4</IPFamily><HostType>IPList</HostType>
#<ListOfIPAddresses>178.128.116.50</ListOfIPAddresses>
#</IPHost></Set></Request>""", verify=False)
#print(response.text)



#Get the IP list for Threat intel IPs:
response=requests.get("""https://172.16.16.16:4444/webconsole/APIController?reqxml=<Request><Login><Username>adminapi</Username><Password>password</Password></Login><Get><IPHost><Name>Threat-intel-IPs</Name><IPFamily>IPv4</IPFamily><HostType>IPList</HostType><ListOfIPAddresses></ListOfIPAddresses></IPHost></Get></Request>""",verify=False)
myroot = ET.fromstring(response.text)
for x in myroot.iter('ListOfIPAddresses'):
	print(x.text)
ipaddr=x.text
#ipaddrr="5.5.5.5"
print(response.text)

ipaddrrr = ipaddr + "," + ipaddrr
#Update the IP list in Threat intel IPs:
response=requests.get("""https://172.16.16.16:4444/webconsole/APIController?reqxml=<Request><Login><Username>adminapi</Username>
<Password>password</Password></Login><Set operation="update"><IPHost><Name>Threat-intel-IPs</Name>
<IPFamily>IPv4</IPFamily><HostType>IPList</HostType>
<ListOfIPAddresses>"""+ipaddrrr+"""</ListOfIPAddresses></IPHost></Set></Request>""",verify=False)
print(response.text)
