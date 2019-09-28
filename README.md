# pythom-metahash
Library for MetaHash in Python

Генерация ключей

+    metahash.gen_pem ()
    генерирует приватный ключ pem

+    metahash.get_pub ( prvpem )
    получает pub ключ из приватного pem

+    metahash.get_address ( pubpem )
    получает MetaHash адрес

+    metahash.pem_to_ecpriv ( prvpem )
    получает приватный ключ для metagate с паролем

+    metahash.ecpriv_to_pem ( ecpriv )
    получает открытый приватный ключ prvpem

+    metahash.pem_to_der ( prvpem )
    получает приватный ключ в формате HEX

    metahash.der_to_pem ( prvder )
    получает pem из HEX

*    metahash.pub_to_der ( pubder )
    получает публичный ключ в формате HEX

    metahash.generate ()
    генерирует prvpem, prvpub ключи

JSON запросы

    metahash.fetch_balance ( net, address )

    metahash.fetch_history ( net, address )

    metahash.get_tx ( net, txhash )

    metahash.create_tx ( net, to, value, privkey, nonce, fee, data )

    metahash.send_tx ( net, to, value, privkey, nonce, fee, data )
