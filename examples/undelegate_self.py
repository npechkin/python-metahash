#!/usr/bin/python3
import os
import sys
import json
import metahash
from getpass import getpass
################################################
net = 'main'
address = '0x00ffaca83513356a14d91f95f46a40aa73b06d5f32359de1d0'
#passwd = '12345' # for *.ec.priv
passwd = getpass ("password:") # for *.ec.priv
################################################
# for Metagate Key
f = open ( address+".ec.priv" )
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )
################################################
to = address
value = '0'
fee = '0'
nonce = metahash.fetch_balance( net, address )['result']['count_spent'] + 1
data = '{"method":"undelegate"}'
res = metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )
result = json.dumps ( res )
print ( result )
