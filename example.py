#!/usr/bin/python3
################################################
net = 'main'
address = '0x00f0bec7a7b832d4400455229103c6cec3abd6736f60152b6d'
# passwd = '12345'
################################################
import os
import json
import metahash
##############  KEY GENERATE  ##################
#address = metahash.generate ()
##############  KEY CONVERT   ##################
#address = metahash.get_address ( address+'.pub' )
#address = metahash.pem_to_pub ( address+'.pem' )
#address = metahash.pem_to_ecpriv ( address+'.pem', passwd )
#address = metahash.ecpriv_to_pem ( address+'.ec.priv', passwd )
#address = metahash.pem_to_der ( address+'.pem' )
#address = address = metahash.pub_to_der ( address+'.pub' )
### metahash.der_to_pem ( address+'.prv.der' )
#################################################
#print ( address )
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

response = metahash.mhc_send ( net,  )
print ( response )
