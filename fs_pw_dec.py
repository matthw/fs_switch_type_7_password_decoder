#!/usr/bin/env python3
# decrypt fs.com type 7 passwords.
# should work on S3700, S3400, S3260, S3150 (tested on S3700)
#
# ex:  
# % ./fs_pw_dec.py 091e333e434451542d4024162b51535c5945
# My_super_P4ssword
#
# by @matth_walter


import sys

KEY = b"JoanCheungOscar\x00"


def fs_pw_dec(password):
    try:
        enc_pwd = bytes.fromhex(password)
    except ValueError:
        return None

    dec_pwd = ""

    if enc_pwd[0] < 0x10:
        salt = enc_pwd[0]
    else:
        salt = enc_pwd[0] - 6

    for c in enc_pwd[1:]:
        d = ((((c - KEY[(salt + (salt >> 4) * -0x10) % len(KEY)]) - salt) + 0xfd) % 0x7f + 0x21) % 0x7f
        dec_pwd += chr(d)
        salt += 1

    return dec_pwd


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("usage: %s <encrypted password>".format(sys.argv[0]))
        sys.exit(0)

    pw = fs_pw_dec(sys.argv[1])
    if pw is None:
        print("error decrypting %s"%sys.argv[1])
        sys.exit(1)

    print(pw)


