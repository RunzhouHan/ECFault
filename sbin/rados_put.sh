#! /bin/bash


dd if=/dev/zero of=./4M  bs=4M  count=16

nmon -f -s 4 -c 800 -g ./nmon_disk_group.dat

it=0
while [ $it -lt 2500 ]
do
	rados -p ecpool put obj_$it 64M 
	let  "it+=1";
done

rm -f ./64M

