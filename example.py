#!/usr/bin/python3
################################################
net = 'main'
address = '0x00ffaca83513356a14d91f95f46a40aa73b06d5f32359de1d0'
# passwd = '12345' # for *.ec.priv
################################################
import os
import sys
import json
import metahash
##############  KEY GENERATE  ##################
#address = metahash.generate ()
##############  KEY CONVERT   ##################
#f = open ( address+".pem" )
#private_key_ascii = f.read()
#public_key_ascii = metahash.pem_to_pub ( private_key_ascii )
#print ( public_key_ascii )

#address = metahash.get_address ( public_key_ascii )

#f = open ( address+".pem" )
#private_key_ascii = f.read()
#ecpriv_key_ascii = metahash.pem_to_ecpriv ( private_key_ascii, passwd )
#f = open ( address+".ec.priv", 'w' )
#f.write ( ecpriv_key_ascii )

#f = open ( address+".ec.priv" )
#ecpriv_key_ascii = f.read()
#private_key_ascii = metahash.ecpriv_to_pem ( ecpriv_key_ascii, passwd )
#f = open ( address+".pem", 'w' )
#f.write ( private_key_ascii )

#f = open ( address+".pem" )
#private_key_ascii = f.read()
#private_der_ascii = metahash.pem_to_der ( private_key_ascii )
#print ( private_der_ascii )

#f = open ( address+".pub" )
#public_key_ascii = f.read()
#public_der_ascii = metahash.pub_to_der ( public_key_ascii )
#print ( public_der_ascii )

#private_der_ascii = '30740201010420---------------------'
#private_key_ascii = metahash.der_to_pem ( private_der_ascii )
#print ( private_key_ascii )
#################################################
#print ( '\n' + address )
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

#to = '0x0088825ae25e516a34cb94bada9b25a811213b55ae3160c888'
#response = metahash.mhc_send ( net, to, value, privkey, nonce, fee, data )
#print ( response )

####################   END   ######################
