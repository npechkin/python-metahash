#!/usr/bin/python3
import os
import sys
import time
import json
import metahash
from getpass import getpass
################################################
net = 'main'
address = '0x00'
#passwd = '12345' # for *.ec.priv
passwd = getpass ("password: ") # for *.ec.priv
node = '0x00f0bec7a7b832d4400455229103c6cec3abd6736f60152b6d'
amount = '0' # 0 = ALL
################################################
f = open ( address+".ec.priv" )
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )
################################################
to = node
value = '0'
fee = '0'
balance = metahash.fetch_balance ( net, address )['result']
bal = balance['received'] - balance['spent']
if bal == 0:
    print ("Balance = 0. Exiting.")
    sys.exit()
print ("Balance =",str(bal/1000000),"MHC. Undelegating.")
nonce = balance['count_spent'] + 1
data = '{"method":"undelegate"}'
res = metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )
result = json.dumps ( res )
print ( result )
print ("Wait 5 second...")
time.sleep (5)
if amount == '0':
    balance = metahash.fetch_balance ( net, address )['result']
    bal = balance['received'] - balance['spent']
    if bal == 0:
        print ("Balance = 0. Exiting.")
        sys.exit()
    amount = str(bal)
print ("Balance =",str(bal/1000000),"MHC. Delegating.")
nonce = nonce + 1
data = '{"method":"delegate","params":{"value":"'+str(bal)+'"}}'
res = metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )
result = json.dumps ( res )
print ( result )
