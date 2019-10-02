Metahash library in Python

Generate private key

[+]    priv_key = metahash.generate () # generate private key

Get public key

[+]    pub_key = metahash.get_public_key ( priv_key ) # returns public key

Get metahash address

[+]    metahash.get_address ( pub_key ) # returns MetaHash address

Dump keys to various formats

[+]    prv_pem_ascii = metahash.dmp_prv_pem ( priv_key )

[+]    ec_prv_pem_ascii = metahash.dmp_ec_prv_pem ( priv_key ) # for Metagate

[+]    prv_der_ascii = metahash.dmp_prv_der ( priv_key ) # for Nodes

[-]    ec_prv_der_ascii = metahash.dmp_ec_prv_der ( priv_key )

Load keys from ascii ( file )

[+]    priv_key = metahash.get_prv_pem ( prv_pem_ascii ) # private key PEM

[+]    priv_key = metahash.get_ec_prv_pem ( prv_pem_ascii, passwd ) # from MetaGate with password

[+]    priv_key = metahash.get_prv_der ( prv_der_ascii ) # from node hex format DER

[-]    priv_key = metahash.get_ec_prv_der ( ec_prv_der_ascii, passwd ) # hex format with password

JSON query

[+]    metahash.fetch_balance ( net, address )

[+]    metahash.fetch_history ( net, address )

[+]    metahash.get_tx ( net, txhash )

[+]    metahash.get_block_by_hash ( net, bkhash, type, beginTx, countTxs )

[+]    metahash.get_block_by_number ( net, block_number, type, beginTx, countTxs )

Sending MHC

[-]    metahash.mhc_send ( net, to, value, privkey, nonce, fee, data )


