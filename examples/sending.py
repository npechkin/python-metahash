#!/usr/bin/python3
import os
import sys
import json
import metahash
from getpass import getpass
################################################
net = 'main'
address = '0x00ffaca83513356a14d91f95f46a40aa73b06d5f32359de1d0'
passwd = '12345' # for *.ec.priv
#passwd = getpass ("password:") # for *.ec.priv
value = '0' # 1 MHC = 1000000
##############  KEY GENERATE  ##################
#priv_key = metahash.generate ()
#################  KEY LOAD   ##################
## EC PEM private key
f = open ( address+".ec.priv" )
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )
##################   SEND MHC   ###################

to = '0x0088825ae25e516a34cb94bada9b25a811213b55ae3160c888'
fee = '0'
nonce = metahash.fetch_balance( net, address )['result']['count_spent'] + 1
data = ''
res = metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )
result = json.dumps ( res )
print ( result )

####################   END   ######################
