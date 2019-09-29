Библиотека функций MetaHash

Генерация ключей

+    metahash.generate ()
    генерирует pem, pub ключи

Конвертация ключей

+    metahash.get_address ( address+'.pub' )
    получает MetaHash адрес из публичного ключа

+    metahash.pem_to_pub ( address+'.pem' )
    получает pub ключ из приватного pem

+    metahash.pem_to_ecpriv ( address+'.pem', passwd )
    получает приватный ключ для MetaGate с паролем

+    metahash.ecpriv_to_pem ( address+'.ec.priv', passwd )
    получает открытый приватный ключ pem

+    metahash.pem_to_der ( address+'.pem' )
    получает приватный ключ в формате HEX der

*    metahash.pub_to_der ( address+'.pub' )
    получает публичный ключ в формате HEX der

    metahash.der_to_pem ( address+'.prv.der' )
    получает pem из HEX der

JSON запросы

+    metahash.fetch_balance ( net, address )

+    metahash.fetch_history ( net, address )

+    metahash.get_tx ( net, txhash )

+    metahash.get_block_by_hash ( net, bkhash, type, beginTx, countTxs )

+    metahash.get_block_by_number ( net, block_number, type, beginTx, countTxs )

    metahash.mhc_send ( net, to, value, privkey, nonce, fee, data )
