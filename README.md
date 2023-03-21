# Decrypt and crypt BDCOM/FS Switch type 7 passwords 
# S3700, S3400, S3260, S3150

this script encrypt and decrypt type 7 passwords on [FS](https://wwww.fs.com/) switches
as well as on [BDCOM](https://www.bdcom.cn) switches.

should work the following FS series:
- S3150
- S3260
- S3400
- S3700

and probably most BDCOM ones ?





example:
```
decrypt:
   ./fs_type_7.py -d 091e333e434451542d4024162b51535c5945
   My_super_P4ssword

encrypt:
   ./fs_type_7.py -e My_super_P4ssword -s 9
   091e333e434451542d4024162b51535c5945
```

read more: [here](https://matth.dmz42.org/posts/2022/reversing-firmwares-from-fs-and-bdcom-switches/)
