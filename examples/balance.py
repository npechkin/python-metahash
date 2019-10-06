#!/usr/bin/python3
import os
import sys
import json
import metahash
from getpass import getpass
################################################
net = 'main'
address = '0x00'
################################################
balance = metahash.fetch_balance(net,address)['result']
bal = (balance['received'] - balance['spent'])/1000000
deleg = (balance['delegate'] - balance['undelegate'])/1000000
nonce = balance['count_spent'] + 1
#print (balance)
print ("Balance =",bal,"MHC. Frozen in delegations",deleg,"MHC. nonce =",nonce)
