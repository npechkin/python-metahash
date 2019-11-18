Metahash library in Python

Generate private key

+    priv_key = metahash.generate () # generate private key

Get public key

+    pub_key = metahash.get_public_key ( priv_key ) # returns public key

Get metahash address

+    metahash.get_address ( pub_key ) # returns MetaHash address

Load keys from ascii ( file )

+    priv_key = metahash.get_prv_pem ( prv_pem_ascii ) # private key PEM

+    priv_key = metahash.get_ec_prv_pem ( prv_pem_ascii, passwd ) # from MetaGate with password

+    priv_key = metahash.get_prv_der ( prv_der_ascii ) # from node hex format DER

+    pub_key = metahash.get_pub_pem ( pub_pem_ascii )

+    pub_key = metahash.get_pub_der ( pub_der_ascii )

Dump keys to various formats

+    prv_pem_ascii = metahash.dmp_prv_pem ( priv_key )

+    ec_prv_pem_ascii = metahash.dmp_ec_prv_pem ( priv_key ) # for Metagate

+    prv_der_ascii = metahash.dmp_prv_der ( priv_key ) # for Nodes

+    pub_pem_ascii = metahash.dmp_pub_pem ( pub_key )

+    pub_der_ascii = metahash.dmp_pub_der ( pub_key )

JSON query

+    metahash.fetch_balance ( net, address )

+    metahash.fetch_history ( net, address, beginTx, countTxs )

+    metahash.fetch_all_history ( net, address )

+    metahash.get_address_delegations ( net, address, beginTx, countTxs )

+    metahash.get_tx ( net, txhash )

+    metahash.get_block_by_hash ( net, bkhash, type, beginTx, countTxs )

+    metahash.get_block_by_number ( net, block_number, type, beginTx, countTxs )

+    metahash.get_last_node_stat_result ( net, address )

+    metahash.get_all_last_nodes_count ( net )

Sending MHC

+    metahash.mhc_send ( net, to, value, fee, nonce, data, priv_key )


