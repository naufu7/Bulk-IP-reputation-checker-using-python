import dns.resolver
import sys

# If you wants to add more RBL's, please list in the below list

bls = ["zen.spamhaus.org", "spam.abuse.ch", "cbl.abuseat.org", "virbl.dnsbl.bit.nl", "dnsbl.inps.de", 
    "ix.dnsbl.manitu.net", "dnsbl.sorbs.net", "bl.spamcop.net", 
    "xbl.spamhaus.org", "pbl.spamhaus.org", "dnsbl-1.uceprotect.net",
    "dnsbl-3.uceprotect.net", "db.wpbl.info","spam.dnsbl.sorbs.net","b.barracudacentral.org","ips.backscatterer.org"]

fh = open("ips.txt",'r')   #Please list the IPs on this text file line by line.

for i  in fh:
   for bl in bls:
     try:
        my_resolver = dns.resolver.Resolver()
        i=i.strip()
        query = '.'.join(reversed(str(i).split("."))) + "." + bl
        req = '.'.join(reversed(str(i).split("."))) + ".in-addr.arpa"
        host = my_resolver.query(req,"PTR")
        answer_txt = my_resolver.query(query, "TXT")
        print('\nhost: %s IS listed in %s => (%s)' %(host[0], bl,answer_txt[0]))
     except dns.resolver.NXDOMAIN:
       pass #Null statement
     except dns.exception.Timeout:
       print('\nThe connection hit a timeout. Are you connected to the internet?\n')
       sys.exit()
