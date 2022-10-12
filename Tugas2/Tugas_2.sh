#!/bin/bash

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
 
