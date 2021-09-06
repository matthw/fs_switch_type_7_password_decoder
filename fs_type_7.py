#!/usr/bin/env python3
#
# encrypt/decrypt bdcom.cn/fs.com type 7 passwords.
# should work on FS S3700, S3400, S3260, S3150 (tested on S3700)
# and most bdcom ones ?
#
# ex:  
# decrypt:
#   ./fs_type_7.py -d 091e333e434451542d4024162b51535c5945
#   My_super_P4ssword
#
# encrypt:
#   ./fs_type_7.py -e My_super_P4ssword -s 9
#   091e333e434451542d4024162b51535c5945
#
# by @matth_walter


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


def fs_pw_enc(salt, password):

    assert salt < 0x10

    enc_pwd = '%02d'%salt

    for c in password:
        d = ((ord(c) - 0x21 + KEY[salt % len(KEY)] + salt) % 0x7f + 1 & 0xff)
        enc_pwd += '%02x'%d
        salt = (salt + 1) & 0xff

    return enc_pwd


if __name__ == "__main__":
    import sys
    import argparse
    from random import randint


    parser = argparse.ArgumentParser(description='Encrypt/decrypt FS type 7 passwords',
                                     prog=sys.argv[0])
    parser.add_argument('password', help='password to encrypt or decrypt')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decrypt', default=False, action='store_true', help='decrypt mode')
    group.add_argument('-e', '--encrypt', default=False, action='store_true', help='encrypt mode')
    parser.add_argument('-s', '--salt', type=int, default=randint(1,16),
                                        choices=range(1,17),
                                        help='salt (1-16) - only for encryption')
    args = parser.parse_args(sys.argv[1:])



    if args.decrypt:
        pw = fs_pw_dec(args.password)
        if pw is None:
            print("error decrypting %s"%sys.argv[1])
            sys.exit(1)

        print(pw)

    elif args.encrypt:
        pw = fs_pw_enc(args.salt, args.password)
        print(pw)


    else:
        print("nop")


