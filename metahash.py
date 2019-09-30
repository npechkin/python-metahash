#!/usr/bin/python3

import os
import sys
if sys.version_info < ( 3,5 ):
    print ( 'You use Python version lower than 3.5. For this script work use Python version 3.5 and more.' )
    exit ( 1 )
import hashlib
import random
import json
import binascii

PROXY = 'proxy.net-%s.metahashnetwork.com'
PROXY_PORT = 9999
TORRENT = 'tor.net-%s.metahashnetwork.com'
TORRENT_PORT = 5795
COUNT_RETRY = 5
###################################################################################
try:
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import ec, padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, NoEncryption, BestAvailableEncryption
    from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_der_private_key, load_pem_public_key, load_der_public_key
except ImportError:
	print ( 'Check your cryptography module installation ( pip install cryptography )' )
	exit ( 1 )
try:
    import dns.resolver
except ImportError:
	print ( 'Check your dnspython module installation ( pip install dnspython )' )
	exit ( 1 )
try:
    import requests
except ImportError:
	print ( 'Check your requests module installation ( pip install requests )' )
	exit ( 1 )

def save_to_file ( text, file_name ):
    with open( file_name, 'w') as f:
        f.write ( text )

def hash_code(code, algth):
    h = hashlib.new(algth)
    h.update(binascii.a2b_hex(code))
    return h.hexdigest()

def hex_point_coordinate ( coordinate_value ):
    value_hex = hex(coordinate_value)
    value_hex = value_hex[2:]
    value_len = 64 - len(value_hex)
    return value_hex if value_len <= 0 else '0' * value_len + value_hex

def generate ():
    private_key = ec.generate_private_key ( ec.SECP256K1(), default_backend() )
    private_key_bin = private_key.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    private_key_ascii = private_key_bin.decode("utf-8")
    public_key_ascii = pem_to_pub ( private_key_ascii )
    address = get_address ( public_key_ascii )
    save_to_file ( private_key_ascii, '%s.pem' % address )
    save_to_file ( public_key_ascii, '%s.pub' % address )
    return ( address )

def get_address ( public_key_ascii ):
    public_key_bin = public_key_ascii.encode("utf-8")
    public_key = load_pem_public_key ( public_key_bin, backend=default_backend() )

    x_hex = hex_point_coordinate ( public_key.public_numbers().x )
    y_hex = hex_point_coordinate ( public_key.public_numbers().y )
    code = '04' + str (x_hex) + str (y_hex)

    resulrt_sha256 = hash_code ( code, 'sha256' )
    resulrt_rmd160 = '00' + hash_code ( resulrt_sha256.encode ( 'utf-8' ), 'rmd160' )
    resulrt_sha256rmd = hash_code(resulrt_rmd160.encode('utf-8'), 'sha256')
    resulrt_sha256rmd_again = hash_code(resulrt_sha256rmd.encode('utf-8'), 'sha256')
    first4_resulrt_sha256rmd_again = resulrt_sha256rmd_again[:8]
    address = '0x' + resulrt_rmd160 + first4_resulrt_sha256rmd_again
    return ( address )

def pem_to_pub ( private_key_ascii ):
    private_key_bin = private_key_ascii.encode("utf-8")
    private_key = load_pem_private_key ( private_key_bin, password=None, backend=default_backend() )
    public_key = private_key.public_key ()
    public_key_bin = public_key.public_bytes ( encoding = Encoding.PEM, format = PublicFormat.SubjectPublicKeyInfo )
    public_key_ascii = public_key_bin.decode("utf-8")
    return ( public_key_ascii )

def pem_to_ecpriv ( private_key_ascii, passwd ):
    passw = passwd.encode("utf-8")
    private_key_bin = private_key_ascii.encode("utf-8")
    private_key = load_pem_private_key ( private_key_bin, password=None, backend=default_backend() )
    ecpriv_key_bin = private_key.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = BestAvailableEncryption ( passw ) )
    ecpriv_key_ascii = ecpriv_key_bin.decode("utf-8")
    return ( ecpriv_key_ascii )

def ecpriv_to_pem ( ecpriv_key_ascii, passwd ):
    passw = passwd.encode("utf-8")
    ecpriv_key_bin = ecpriv_key_ascii.encode("utf-8")
    private_key = load_pem_private_key ( ecpriv_key_bin, password=passw, backend=default_backend() )
    private_key_bin = private_key.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    private_key_ascii = private_key_bin.decode("utf-8")
    return ( private_key_ascii )

def pem_to_der ( private_key_ascii ):
    private_key_bin = private_key_ascii.encode ("utf-8")
    private_key = load_pem_private_key ( private_key_bin, password=None, backend=default_backend() )
    private_der_bytes = private_key.private_bytes ( encoding = Encoding.DER, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    private_der_bin = binascii.b2a_hex ( private_der_bytes )
    private_der_ascii = private_der_bin.decode ( )
    return ( private_der_ascii )

def pub_to_der ( public_key_ascii ):
    public_key_bin = public_key_ascii.encode ("utf-8")
    public_key = load_pem_public_key ( public_key_bin, backend=default_backend() )
    public_der_bin = public_key.public_bytes ( encoding = Encoding.DER, format = PublicFormat.SubjectPublicKeyInfo )
    public_der_ascii = binascii.b2a_hex(public_der_bin).decode()
    return ( public_der_ascii )

def der_to_pem ( private_der_ascii ):
    private_der_bin = private_der_ascii.encode ("utf-8")
    private_der_bytes = binascii.a2b_hex ( private_der_bin )
    private_key = load_der_private_key ( private_der_bytes, password=None, backend=default_backend() )
    private_key_bin = private_key.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    private_key_ascii = private_key_bin.decode ( )
    return ( private_key_ascii )

def torrent_request ( net, request ):
    addr = TORRENT % net
    items = dns.resolver.Resolver().query(addr).rrset.items
    ip_addr = items[0].address
    url = "http://" + ip_addr + ":%d" % ( TORRENT_PORT )
    data = json.dumps ( request )
    r = requests.post ( url, data )
    result = json.loads ( r.text )
    return ( result )

def proxy_request ( net, request ):
    addr = PROXY % net
    items = dns.resolver.Resolver().query(addr).rrset.items
    ip_addr = items[0].address
    url = "http://" + ip_addr + ":%d" % ( PROXY_PORT )
    data = json.dumps ( request )
    r = requests.post ( url, data )
    result = json.loads ( r.text )
    return ( result )

def fetch_balance ( net, address ):
    request = { "id": 1, "method": "fetch-balance", "params": { "address": address } }
    balance = torrent_request ( net, request )
    return ( balance )

def fetch_history ( net, address, beginTx, countTxs ):
    request = { "id": 1, "method": "fetch-history", "params": { "address": address, "beginTx": beginTx, "countTxs": countTxs } }
    history = torrent_request ( net, request )
    return ( history )

def get_tx ( net, txhash ):
    request = { "id": 1, "method": "get-tx", "params": { "hash": txhash } }
    response = torrent_request ( net, request )
    return ( response )

def get_block_by_hash ( net, bkhash, typ, beginTx, countTxs ):
    request = { "id": 1, "method": "get-block-by-hash", "params": { "hash": bkhash, "type": typ, "beginTx": beginTx, "countTxs": countTxs } }
    response = torrent_request ( net, request )
    return ( response )

def get_block_by_number ( net, block_number, typ, beginTx, countTxs ):
    request = { "id": 1, "method": "get-block-by-number", "params": { "number": block_number, "type": typ, "beginTx": beginTx, "countTxs": countTxs } }
    response = torrent_request ( net, request )
    return ( response )

def mhc_send ( net, to, value, privkey, nonce, fee, data ):
    pubkey = pub_to_der ( p )
    request = { "id": 1, "method": "mhc_send", "params": { "to": to , "value": value, "fee": fee, "nonce": nonce, "data": data, "pubkey": pub_key,"sign": sign } }
    response = proxy_request ( net, request )
    return ( response )

###########################    END    ############################
