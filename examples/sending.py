#!/usr/bin/python3
import os
import sys
import json
import metahash
from getpass import getpass
################################################
net = 'main'
address = '0x00'
#passwd = '12345' # for *.ec.priv
passwd = getpass ("password:") # for *.ec.priv
to = '0x00'
value = '0' # if 0 send ALL
#################  KEY LOAD   ##################
f = open(address+".ec.priv","r")
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )
##################   SEND MHC   ###################
balance = metahash.fetch_balance(net,address)['result']
bal = (balance['received'] - balance['spent'])
if bal == 0:
    print ("Balance = 0. Exiting.")
    sys.exit()
if bal < int(value):
    print("Balance <",str(int(value)/1000000),"Exiting.")
    sys.exit()
if value == '0':
    value = str(bal)
print ("Sending",str(int(value)/1000000),"MHC to", to)
fee = 0
nonce = balance['count_spent'] + 1
data = ''
res = metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )
result = json.dumps ( res )
print ( result )
####################   END   ######################
