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

################################################
## EC PEM private key
f = open ( address+".ec.priv" )
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )

## DER private key  ( for Nodes)
prv_der_ascii = metahash.dmp_prv_der ( priv_key )
#metahash.save_to_file ( prv_der_ascii, '%s.prv.der' % address )
print ( prv_der_ascii )
