# Test

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
    print ( 'Something went wrong, check your cryptography module installation ( pip install cryptography )' )
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

def gen_pem ():

    private_key = ec.generate_private_key ( ec.SECP256K1(), default_backend() )
    private_key_pem = private_key.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    save_to_file ( private_key_pem.decode("utf-8"), 'mhc.pem' )
#    save_to_file ( private_key_pem.decode("utf-8"), "%s.pem" % address )

def get_pub ( prvpem ):
    f = open ( prvpem )
    prv_key = f.read()
    prv_pem = prv_key.encode("utf-8")
    prkey = load_pem_private_key ( prv_pem, password=None, backend=default_backend() )
    pub_key = prkey.public_key ()
    pub_key_pem = pub_key.public_bytes ( encoding = Encoding.PEM, format = PublicFormat.SubjectPublicKeyInfo )
    save_to_file ( pub_key_pem.decode("utf-8"), "mhc.pub" )

def get_address ( pubpem ):
    f = open ( pubpem )
    pkey = f.read()
    pub_key_pem = pkey.encode("utf-8")
    pub_key = load_pem_public_key ( pub_key_pem, backend=default_backend() )

    x_hex = hex_point_coordinate ( pub_key.public_numbers().x )
    y_hex = hex_point_coordinate ( pub_key.public_numbers().y )
    code = '04' + str (x_hex) + str (y_hex)

    resulrt_sha256 = hash_code ( code, 'sha256' )
    resulrt_rmd160 = '00' + hash_code ( resulrt_sha256.encode ( 'utf-8' ), 'rmd160' )
    resulrt_sha256rmd = hash_code(resulrt_rmd160.encode('utf-8'), 'sha256')
    resulrt_sha256rmd_again = hash_code(resulrt_sha256rmd.encode('utf-8'), 'sha256')
    first4_resulrt_sha256rmd_again = resulrt_sha256rmd_again[:8]
    address = '0x' + resulrt_rmd160 + first4_resulrt_sha256rmd_again
    print ( address )

def pub_to_der ( pubpem ):
    f = open ( pubpem )
    pkey = f.read()
    pub_key_pem = pkey.encode("utf-8")
    pub_key = load_pem_public_key ( pub_key_pem, backend=default_backend() )

    pub_key_der = pub_key.public_bytes ( encoding = Encoding.DER, format = PublicFormat.SubjectPublicKeyInfo )
    pk_der = binascii.b2a_hex(pub_key_der).decode()
    save_to_file ( pk_der, "mhc.pub.der" )
#    print ( pk_der )

def pem_to_der ( prvpem ):
    f = open ( prvpem )
    prv_key = f.read()
    prv_pem = prv_key.encode("utf-8")
    prkey = load_pem_private_key ( prv_pem, password=None, backend=default_backend() )

    private_key_der = prkey.private_bytes ( encoding = Encoding.DER, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    pr_der = binascii.b2a_hex(private_key_der).decode()
    save_to_file ( pr_der, "mhc.prv.der" )
#    print ( pr_der )

def ecpriv_to_pem ( ecpriv, passwd ):
    f = open ( ecpriv )
    ecprv_key = f.read()
    prv_pem = ecprv_key.encode("utf-8")
    passw = passwd.encode("utf-8")
    prkey = load_pem_private_key ( prv_pem, password=passw, backend=default_backend() )

    print ( prkey )

    private_key_pem = prkey.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
    save_to_file ( private_key_pem.decode("utf-8"), 'mhc.pem' )
#    print ( private_key_pem )

def pem_to_ecpriv ( prvpem, passwd ):
    f = open ( prvpem )
    prv_key = f.read()
    prv_pem = prv_key.encode("utf-8")
    passw = passwd.encode("utf-8")
    prkey = load_pem_private_key ( prv_pem, password=None, backend=default_backend() )
    print ( prkey )

    ec_priv = prkey.private_bytes ( encoding = Encoding.PEM, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = BestAvailableEncryption ( passw ) )
    save_to_file ( ec_priv.decode("utf-8"), "mhc.ec.priv" )
#    print ( ec_priv )

def der_to_pem ( prvder ):
    f = open ( prvder )
    prv_key = f.read()
    prv_der = prv_key.encode ("utf-8")
    prkey = load_der_private_key ( prv_der, password=None, backend=default_backend() )
    print ( prkey )

#    print ( prv_der )
#    pr_der = binascii.b2a_hex(prv_der).decode()
#    print ( pr_der )



#    private_key_der = prkey.private_bytes ( encoding = Encoding.DER, format = PrivateFormat.TraditionalOpenSSL, encryption_algorithm = NoEncryption() )
#    print ( pr_der )
#    pr_der = binascii.b2a_hex(private_key_der).decode()
#    save_to_file ( pr_der, "mhc.prv.der" )
#    print ( pr_der )





