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
passwd = getpass ("password: ") # for *.ec.priv
amount = '0' # 1 MHC = 1000000; IF 0 THEN DELEGATE ALL
node = '0x00123456bea359caad6bee3903417b3fbdf0fb082e02ac039e'
################################################
# for Metagate Key
f = open ( address+".ec.priv" )
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )
################################################
to = node
balance = metahash.fetch_balance ( net, address )['result']
bal = balance['received'] - balance['spent']
if bal < 512000000:
    print ("Balance less than 512 MHC. Exit.")
    sys.exit ()
if int(amount) > 0:
    if int(amount) < 512000000:
        print ("You can not delegate less than 512 MHC. Exit.")
        sys.exit ()
if bal < int(amount):
    print ("Balance =",str(bal/1000000),"MHC.",str(int(amount)/1000000),"MHC cannot be sent. Exit.")
    sys.exit()
if amount == '0':
    amount = str(bal)
value = '0'
fee = '0'
nonce = balance['count_spent'] + 1
data = '{"method":"delegate","params":{"value":"'+amount+'"}}'
print (data)
res = metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )
result = json.dumps ( res )
print ( result )
