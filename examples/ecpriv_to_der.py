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
##############  KEY GENERATE  ##################
priv_key = metahash.generate ()
#################  KEY LOAD   ##################

## PEM private keys
#f = open ( address+".pem" )
#prv_pem_ascii = f.read()
#priv_key = metahash.get_prv_pem ( prv_pem_ascii )

## EC PEM private key
f = open ( address+".ec.priv" )
ec_prv_pem_ascii = f.read()
priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )

## PEM public key
#f = open ( address+".pub" )
#pub_pem_ascii = f.read()
#pub_key = metahash.get_pub_pem ( pub_pem_ascii )

## DER private key
#prv_der_ascii = '307402010104206ce96125549121883cdb8823a8f9d020249c58d638f92546744f652156ad6840a00706052b8104000aa14403420004f5e084f2ec9e16963b6fc22d687408f233cdbef42cf9d33a7cd8bdff6729d8f9b914c33bf337afcf144dd18bd3212fca05fb802b58253d474a146f1f33761ae1'
#priv_key = metahash.get_prv_der ( prv_der_ascii )

## DER public key
#pub_der_ascii = '3056301006072a8648ce3d020106052b8104000a03420004f5e084f2ec9e16963b6fc22d687408f233cdbef42cf9d33a7cd8bdff6729d8f9b914c33bf337afcf144dd18bd3212fca05fb802b58253d474a146f1f33761ae1'
#pub_key = metahash.get_pub_der ( pub_der_ascii )

############# GET PUBLIC KEY ####################
#pub_key = metahash.get_public_key ( priv_key )
##############  GET ADDRESS   ###################
#address = metahash.get_address ( pub_key )
#print ( address )
#################  KEY DUMP   ##################

## PEM private key
#prv_pem_ascii = metahash.dmp_prv_pem ( priv_key )
#metahash.save_to_file ( prv_pem_ascii, '%s.pem' % address )
#print ( prv_pem_ascii )

## EC PEM private key ( Metagate )
#ec_prv_pem_ascii = metahash.dmp_ec_prv_pem ( priv_key, passwd )
#metahash.save_to_file ( ec_prv_pem_ascii, '%s.ec.priv' % address )
#print ( ec_prv_pem_ascii )

## PEM public keys
#pub_pem_ascii = metahash.dmp_pub_pem ( pub_key )
#metahash.save_to_file ( pub_pem_ascii, '%s.pub' % address )
#print ( pub_pem_ascii )

## DER private key  ( for Nodes)
prv_der_ascii = metahash.dmp_prv_der ( priv_key )
#metahash.save_to_file ( prv_der_ascii, '%s.prv.der' % address )
print ( prv_der_ascii )

## EC DER private key
#ec_prv_der_ascii = metahash.dmp_ec_prv_der ( priv_key, passwd )
#metahash.save_to_file ( ec_prv_der_ascii, '%s.ec.prv.der' % address )
#print ( ec_prv_der_ascii )

## DER public key
#pub_der_ascii = metahash.dmp_pub_der ( pub_key )
#metahash.save_to_file ( pub_der_ascii, '%s.pub.der' % address )
#print ( pub_der_ascii )
