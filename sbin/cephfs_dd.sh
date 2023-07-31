#! /bin/bash


nmon -f -s 4 -c 800 -g ./nmon_disk_group.dat

it=0
while [ $it -lt 10000 ]
do
	dd if=/dev/zero of=./cephfs/4M_$it  bs=4M  count=1
	let  "it+=1";
done

