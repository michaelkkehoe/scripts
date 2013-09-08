#!/usr/bin/env python26
#Written by Simon Coggins (2013)
import os, sys
import dns
import dns.query
import dns.zone
from dns.exception import DNSException
from dns.rdataclass import *
from dns.rdatatype import *
 
 
xfer = dns.query.xfr("ns1.uq.edu.au", "uq.edu.au")
cqu = dns.zone.from_xfr(xfer)
 
Map = {}
 
# Find A records
 
for name, node in cqu.nodes.items():
  for rdataset in node.rdatasets:
    if rdataset.rdclass != IN or rdataset.rdtype not in [A, CNAME, MX]:
      continue
    for rdata in rdataset:
      if rdataset.rdtype == A:
        key = rdata.address
      else:
        key = str(rdata.target)
      if key not in Map:
        Map[key] = []
 
      Map[key].append(str(name).lower())
 
    
 
def recursivePrint(obj, indent=0):
  print "\t"*indent, obj
  if obj in Map:
    for x in Map[obj]:
      recursivePrint(x, indent+1)
 
 
if len(sys.argv) <= 1:
  print "Need a starting point"
  sys.exit(0)
 
recursivePrint(sys.argv[1])
