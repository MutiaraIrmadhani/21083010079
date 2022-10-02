echo "Bilangan positif kelipatan ganjil dengan bilangan acuan 15"
read ganjil;
echo "Input: $ganjil"

a=$ganjil
while [ $a -gt 0 ]
do
   echo $a
   a=$((a-2))
done


