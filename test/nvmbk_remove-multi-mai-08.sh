#!/bin/bash

me=$0
ECFAULT_HOME=$(cd -P -- `dirname $me`/ && pwd -P)

dev=(sda sdb sdc sdd sde sdf sdg sdh sdj)               # physical device name
dev_count=9
target_per_dev=4                                        # number of OSDs
loop_idx=20                                             # start from /dev/loop20, modify per your loop device availability

count=$(($dev_count*$target_per_dev))

$ECFAULT_HOME/nvmetcli/nvmetcli clear


it=0
while [ $it -lt $count ]
do
	losetup -d /dev/loop$(($it+$loop_idx))
	let  "it+=1" 
done

#rm -f $ECFAULT_HOME/img/*

it=0
while [ $it -lt $dev_count ]
do
	#rm -f $ECFAULT_HOME/img/${dev[it]}/*
        let  "it+=1"
done


echo "Removed $count nvme targets"
