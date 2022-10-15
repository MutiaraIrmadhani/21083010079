#!/bin/bash

printf "Operasi matematika apa yang kamu mau?\n"
printf "penjumlahan?\n"
printf "pengurangan?\n"
printf "perkalian?\n"
printf "pembagian?\n"

read operasi
printf "Operasi yang dipilih $operasi\n"
echo "Masukkan nilai a="
read a
echo "masukkan nilai b="
read b

echo
let "hasil = $nilai a * $nilai b";
echo -n "$nilai a x $nilai b adalah $hasil";
echo
echo 
let "hasil = $nilai a + $nilai b";
echo -n "$nilai a + $nilai b adalah $hasil";
echo

if [ $a -eq  $b ]
then
   echo "$a sama dengan $b"
elif [ $a -gt $b ]
then
  echo "$a lebih dari $b"
elif [ $a -lt $b ]
then
   echo "$a kurang dari $b"
else
echo "Tidak ada kondisi yang memenuhi"
fi
 
