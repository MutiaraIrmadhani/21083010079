#!/bin/bash

read -p "Berapa banyak semester yang sudah anda tempuh?" semester
echo "------------------------------------------------------------"

declare -a ips

i=0
let banyak=$semester-1

while [ $i -le $banyak ];
do
  let angka=$i+1
  read -p "Nilai semester $angka:" nilaisemester
  ips[$i]=$nilaisemester;
  let jumlah=jumlah+$nilaisemester;
  let i=$i+1;
done

echo "-------------------------------------------------------------"
let ipk=$jumlah/$semester
echo "Nilai tiap semester secara berurutan :" ${ips[@]}
echo "Nilai IPS :" $jumlah "/" $semester
echo "Nilai IPK :" $ipk
echo "-------------------------------------------------------------"
