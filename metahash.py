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
    priv_key = ec.generate_private_key ( ec.SECP256K1(), default_backend() )
    return ( priv_key )

def get_prv_pem ( prv_pem_ascii ):
    prv_pem_bin = prv_pem_ascii.encode("utf-8")
    priv_key = load_pem_private_key ( prv_pem_bin, password=None, backend=default_backend() )
    return ( priv_key )

def get_prv_der ( prv_der_ascii ):
    prv_der_bin = prv_der_ascii.encode("utf-8")
    prv_der_bytes = binascii.a2b_hex ( prv_der_bin )
    priv_key = load_der_private_key ( prv_der_bytes, password=None, backend=default_backend() )
    return ( priv_key )

def get_ec_prv_pem ( ec_prv_pem_ascii, passwd ):
    passw = passwd.encode("utf-8")
    ec_prv_pem_bin = ec_prv_pem_ascii.encode("utf-8")
    priv_key = load_pem_private_key ( ec_prv_pem_bin, password=passw, backend=default_backend() )
    return ( priv_key )

def get_pub_pem ( pub_pem_ascii ):
    pub_pem_bin = pub_pem_ascii.encode("utf-8")
    pub_key = load_pem_public_key ( pub_pem_bin, backend=default_backend() )
    return ( pub_key )

def get_pub_der ( pub_der_ascii ):
    pub_der_bin = pub_der_ascii.encode("utf-8")
    pub_der_bytes = binascii.a2b_hex ( pub_der_bin )
    pub_key = load_der_public_key ( pub_der_bytes, backend=default_backend() )
    return ( pub_key )

def dmp_prv_der ( priv_key ):
    prv_der_bytes = priv_key.private_bytes ( encoding = Encoding.DER, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    prv_der_bin = binascii.b2a_hex ( prv_der_bytes )
    prv_der_ascii = prv_der_bin.decode ( )
    return ( prv_der_ascii )

def dmp_prv_pem ( priv_key ):
    prv_pem_bin = priv_key.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    prv_pem_ascii = prv_pem_bin.decode("utf-8")
    return ( prv_pem_ascii )

def dmp_ec_prv_pem ( priv_key, passwd ):
    passw = passwd.encode("utf-8")
    ec_prv_pem_bin = priv_key.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = BestAvailableEncryption ( passw ) )
    ec_prv_pem_ascii = ec_prv_pem_bin.decode("utf-8")
    return ( ec_prv_pem_ascii )

def dmp_pub_pem ( pub_key ):
    pub_pem_bin = pub_key.public_bytes ( encoding = Encoding.PEM, format = PublicFormat.SubjectPublicKeyInfo )
    pub_pem_ascii = pub_pem_bin.decode("utf-8")
    return ( pub_pem_ascii )

def dmp_pub_der ( pub_key ):
    pub_der_bytes = pub_key.public_bytes ( encoding = Encoding.DER, format = PublicFormat.SubjectPublicKeyInfo )
    pub_der_bin = binascii.b2a_hex ( pub_der_bytes )
    pub_der_ascii = pub_der_bin.decode ( )
    return ( pub_der_ascii )

def get_public_key ( priv_key ):
    pub_key = priv_key.public_key ()
    return ( pub_key )

def get_address ( pub_key ):
    x_hex = hex_point_coordinate ( pub_key.public_numbers().x )
    y_hex = hex_point_coordinate ( pub_key.public_numbers().y )
    code = '04' + str (x_hex) + str (y_hex)
    resulrt_sha256 = hash_code ( code, 'sha256' )
    resulrt_rmd160 = '00' + hash_code ( resulrt_sha256.encode ( 'utf-8' ), 'rmd160' )
    resulrt_sha256rmd = hash_code(resulrt_rmd160.encode('utf-8'), 'sha256')
    resulrt_sha256rmd_again = hash_code(resulrt_sha256rmd.encode('utf-8'), 'sha256')
    first4_resulrt_sha256rmd_again = resulrt_sha256rmd_again[:8]
    address = '0x' + resulrt_rmd160 + first4_resulrt_sha256rmd_again
    return ( address )

def torrent_request ( net, request ):
    url = 'http://tor.net-'+net+'.metahashnetwork.com:5795'
    headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
    data = json.dumps ( request )
    res = requests.post ( url, data, headers = headers )
    result = json.loads ( res.text )
    return ( result )

def proxy_request ( net, request ):
    url = 'http://proxy.net-'+net+'.metahashnetwork.com:9999'
    headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
    data = json.dumps ( request )
    res = requests.post ( url, data, headers = headers )
    result = json.loads ( res.text )
    return ( result )

def fetch_balance ( net, address ):
    request = {'id':1,'method':'fetch-balance','params':{'address':address}}
    balance = torrent_request ( net, request )
    return ( balance )

def fetch_history ( net, address, beginTx, countTxs ):
    request = {'id':1,'method':'fetch-history','params':{'address':address,'beginTx':beginTx,'countTxs':countTxs}}
    history = torrent_request ( net, request )
    return ( history )

def get_tx ( net, txhash ):
    request = {'id':1,'method':'get-tx','params':{'hash':txhash}}
    response = torrent_request ( net, request )
    return ( response )

def get_block_by_hash ( net, bkhash, typ, beginTx, countTxs ):
    request = {'id':1,'method':'get-block-by-hash','params':{'hash':bkhash,'type':typ,'beginTx':beginTx,'countTxs':countTxs}}
    response = torrent_request ( net, request )
    return ( response )

def get_block_by_number ( net, block_number, typ, beginTx, countTxs ):
    request = {'id':1,'method':'get-block-by-number','params':{'number':block_number,'type':typ,'beginTx':beginTx,'countTxs':countTxs}}
    response = torrent_request ( net, request )
    return ( response )

def little_ending ( bytes ):
    res_str = ''
    while len ( bytes ):
        res_str += bytes [-2:]
        bytes = bytes [:-2]
    return res_str

def int_to_hex(value):
    low_border = 250
    read_int16 = 'fa'
    read_int32 = 'fb'
    read_int64 = 'fc'
    read_int128 = 'fd'
    read_int256 = 'fe'
    read_int512 = 'ff'
    bit = value.bit_length()
    if value < low_border:
        return '%02x' % value
    elif value >= low_border and bit <= 16:
        return read_int16 + little_ending('%.4x' % value)
    elif bit > 16 and bit <= 32:
        return read_int32 + little_ending('%.8x' % value)
    elif bit > 32 and bit <= 64:
        return read_int64 + little_ending('%.16x' % value)
    elif bit > 64 and bit <= 128:
        return read_int128 + little_ending('%.32x' % value)
    elif bit > 128 and bit <= 256:
        return read_int256 + little_ending('%.64x' % value)
    elif bit > 256 and bit <=512:
        return read_int512 + little_ending('%.128x' % value)

def get_sign ( to, value, fee, nonce, dataHex, priv_key ):
    len_data = int(len(dataHex)/2)
    sign_text = ''
    sign_text += to[2:]
    sign_text += int_to_hex(int(value))
    sign_text += int_to_hex(fee)
    sign_text += int_to_hex(nonce)
    sign_text += int_to_hex(len_data)
    sign_text += dataHex

    bytes_text = binascii.unhexlify(sign_text)
    signature = priv_key.sign ( bytes_text, ec.ECDSA ( hashes.SHA256() ) )
    sign = binascii.b2a_hex (signature).decode()
    return (sign)

def mhc_send ( net, to, value, fee, nonce, data, priv_key ):
    pub_key = get_public_key ( priv_key )
    pub_der_ascii = dmp_pub_der ( pub_key )

    byte_data = str.encode ( data )
    hex_data = binascii.hexlify ( byte_data )
    dataHex = hex_data.decode ()
    fee = len(dataHex)
    sign = get_sign ( to, value, fee, nonce, dataHex, priv_key )

    req = {'id':1,'method':'mhc_send','params':{'to':to,'value':value,'fee':str(fee),'nonce':str(nonce),'data':dataHex,'pubkey':pub_der_ascii,'sign':sign}}
    res = proxy_request ( net, req )
    return ( res )

###########################    END    ############################
