#!/usr/bin/python3

import os
import json
import metahash

prvpem = 'mhc.pem'
pubpem = 'mhc.pub'
prvder = "mhc.prv.der"
passwd = '123456789'
net = 'main'
data = ''
fee = 0

metahash.gen_pem ()
metahash.get_pub ( prvpem )
metahash.get_address ( pubpem )
#metahash.pub_to_der ( pubpem )
#metahash.pem_to_der ( prvpem )
#metahash.ecpriv_to_pem ( ecpriv, passwd )
metahash.pem_to_ecpriv ( prvpem, passwd )
#metahash.der_to_pem ( prvder )

