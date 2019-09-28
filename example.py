#!/usr/bin/python3
################################################
address = '0x00fef840b43395bfb0a1d3d7b119cefef71d2dc4f959e5c6e7'
passwd = '12345'
################################################
import os
import json
import metahash

##############  KEY GENERATE  ##################

address = metahash.generate ()

##############  KEY CONVERT   ##################

#address = metahash.get_address ( address+'.pub' )

#address = metahash.pem_to_pub ( address+'.pem' )

#metahash.pem_to_ecpriv ( address+'.pem', passwd )

#metahash.ecpriv_to_pem ( address+'.ec.priv', passwd )

#metahash.pem_to_der ( address+'.pem' )

#address = metahash.pub_to_der ( address+'.pub' )

#metahash.der_to_pem ( address+'.prv.der' )

#################################################

print ( address )

#################################################
