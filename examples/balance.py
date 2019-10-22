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
beginTx = 0
countTxs = 256
delegations = metahash.get_address_delegations( net, address, beginTx, countTxs )['result']['states']

print ("Balance =",bal,"MHC. nonce =",nonce)
print ("Frozen in delegations",deleg,"MHC. Delegations count",str(len(delegations)),"from 256.")
