#!/bin/python3
import requests

response=requests.get("""https://172.16.16.16:4444/webconsole/APIController?reqxml=<Request><Login><Username>adminapi</Username>
<Password>Test@3706653</Password></Login><Set operation="update"><IPHost><Name>Threat-intel-IPs</Name>
<IPFamily>IPv4</IPFamily><HostType>IPList</HostType>
<ListOfIPAddresses>1.2.3.4,2.3.5.4,178.128.116.50</ListOfIPAddresses>
</IPHost></Set></Request>""", verify=False)
print(response.text)
