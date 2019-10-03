#!/usr/bin/python3
################################################
import os
import sys
import json
import metahash
################################################
net = 'main'
address = '0x00ffaca83513356a14d91f95f46a40aa73b06d5f32359de1d0'
#passwd = '12345' # for *.ec.priv
##############  KEY GENERATE  ##################
#priv_key = metahash.generate ()
############# GET PUBLIC KEY ####################
#pub_key = metahash.get_public_key ( priv_key )
##############  GET ADDRESS   ###################
#address = metahash.get_address ( pub_key )
#print ( address )
#################  KEY LOAD   ##################
## PEM private keys
f = open ( address+".pem" )
prv_pem_ascii = f.read()
priv_key = metahash.get_prv_pem ( prv_pem_ascii )

## EC PEM private key
#f = open ( address+".ec.priv" )
#ec_prv_pem_ascii = f.read()
#priv_key = metahash.get_ec_prv_pem ( ec_prv_pem_ascii, passwd )

## DER private key
prv_der_ascii = '307402010104206ce96125549121883cdb8823a8f9d020249c58d638f92546744f652156ad6840a00706052b8104000aa14403420004f5e084f2ec9e16963b6fc22d687408f233cdbef42cf9d33a7cd8bdff6729d8f9b914c33bf337afcf144dd18bd3212fca05fb802b58253d474a146f1f33761ae1'
priv_key = metahash.get_prv_der ( prv_der_ascii )

## PEM public key
#f = open ( address+".pub" )
#pub_pem_ascii = f.read()
#pub_key = metahash.get_pub_pem ( pub_pem_ascii )

## DER public key
#pub_der_ascii = '3056301006072a8648ce3d020106052b8104000a03420004f5e084f2ec9e16963b6fc22d687408f233cdbef42cf9d33a7cd8bdff6729d8f9b914c33bf337afcf144dd18bd3212fca05fb802b58253d474a146f1f33761ae1'
#pub_key = metahash.get_pub_der ( pub_der_ascii )

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
#prv_der_ascii = metahash.dmp_prv_der ( priv_key )
#metahash.save_to_file ( prv_der_ascii, '%s.prv.der' % address )
#print ( prv_der_ascii )

## DER public key
#pub_der_ascii = metahash.dmp_pub_der ( pub_key )
#metahash.save_to_file ( pub_der_ascii, '%s.pub.der' % address )
#print ( pub_der_ascii )

################   GET INFO   ###################
#balance = metahash.fetch_balance ( net, address )
#nonce = balance['result']['count_spent'] + 1
#print ( "nonce = %s" % nonce )

#beginTx = 0
#countTxs = 10 # max 9999
#history = metahash.fetch_history ( net, address, beginTx, countTxs )
#print ( history )

#txhash = 'acb509298c8e83042b3609553d83fbaf5c1179f167b26eaf0993f86ed1729cfb'
#response = metahash.get_tx ( net, txhash )
#print ( response )

#typ = 1 # 0-4
#beginTx = 0
#countTxs = 2
#bkhash = '49a840968be1a3c0449a6d7946fd021ce2746006ff5b855fdc0623669833f5e7'
#response = metahash.get_block_by_hash ( net, bkhash, typ, beginTx, countTxs )
#print ( response )

#typ = 1 # 0-4
#beginTx = 0
#countTxs = 2
#block_number = 1000000
#response = metahash.get_block_by_number ( net, block_number, typ, beginTx, countTxs )
#print ( response )

##################   SEND MHC   ###################

to = '0x0088825ae25e516a34cb94bada9b25a811213b55ae3160c888'
value = '0'
nonce = metahash.fetch_balance( net, address )['result']['count_spent'] + 1
fee = '0'
data = ''
res = metahash.mhc_send ( net, to, value, priv_key, nonce, fee, data )
result = json.dumps ( res )
print ( result )

####################   END   ######################
