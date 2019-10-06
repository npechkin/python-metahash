#!/usr/bin/python3
import os
import sys
import json
import metahash
from getpass import getpass
################################################
net = 'main'
address = '0x008288d035e4b4b8a043b27dd4487e3440894eaaa3044de888'
################################################
balance = metahash.fetch_balance(net,address)['result']
bal = (balance['received'] - balance['spent'])/1000000
deleg = (balance['delegate'] - balance['undelegate'])/1000000
nonce = balance['count_spent'] + 1
#print (balance)
print ("Balance =",bal,"MHC. Frozen in delegations",deleg,"MHC. nonce =",nonce)
