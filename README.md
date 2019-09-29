Библиотека функций MetaHash

Генерация ключей

+    metahash.generate ()
    генерирует pem, pub ключи, записывает их на диск

Конвертация ключей

+    metahash.get_address ( public_key_ascii )
    возвращает MetaHash адрес из публичного ключа

+    metahash.pem_to_pub ( private_key_ascii )
    возвращает pub ключ из приватного pem

+    metahash.pem_to_ecpriv ( private_key_ascii, passwd )
    возвращает приватный ключ для MetaGate с паролем

+    metahash.ecpriv_to_pem ( ecpriv_key_ascii, passwd )
    возвращает открытый приватный ключ pem

+    metahash.pem_to_der ( private_key_ascii )
    возвращает приватный ключ в формате HEX der

*    metahash.pub_to_der ( public_key_ascii )
    возвращает публичный ключ в формате HEX der

    metahash.der_to_pem ( private_der_ascii )
    возвращает pem из HEX der

JSON запросы

+    metahash.fetch_balance ( net, address )

+    metahash.fetch_history ( net, address )

+    metahash.get_tx ( net, txhash )

+    metahash.get_block_by_hash ( net, bkhash, type, beginTx, countTxs )

+    metahash.get_block_by_number ( net, block_number, type, beginTx, countTxs )

    metahash.mhc_send ( net, to, value, privkey, nonce, fee, data )
