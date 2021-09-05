# Decrypt and crypt FS Switch type 7 passwords (S3700, S3400, S3260, S3150)

this script encrypt and decrypt type 7 passwords on [FS](https://wwww.fs.com/) switches.

tested on a [S3700](https://www.fs.com/products/84912.html) model

should also work the following series:
- S3150
- S3260
- S3400

example:
```
decrypt:
   ./fs_type_7.py -d 091e333e434451542d4024162b51535c5945
   My_super_P4ssword

encrypt:
   ./fs_type_7.py -e My_super_P4ssword -s 9
   091e333e434451542d4024162b51535c5945
```

