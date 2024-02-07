#!/bin/bash

# This script creates NVMe TCP targets


# Need nvme-tcp kernel modules
modprobe nvme_tcp
modprobe nvmet
modprobe nvmet_tcp


me=$0
ECFAULT_HOME=$(cd -P -- `dirname $me`/ && pwd -P)


# Configuration # 
dev=(sda sdb sdc sdd sde sdf sdg sdh sdj)								# physical device name
dev_count=9
target_per_dev=2 					# number of OSDs
target_sz=10240							# OSD size
conn="tcp" 							# connection type
addr_traddr="10.24.86.175" 						# target host ip addr
loop_idx=20 						# start from /dev/loop20, modify per your loop device availability


mkdir -p $ECFAULT_HOME/img

curr=0
it=0

while [ $curr -lt $dev_count ]
do
 	#mkdir -p $ECFAULT_HOME/img/${dev[curr]}
	#mount /dev/${dev[curr]} $ECFAULT_HOME/img/${dev[curr]}


	curr_count=0
	while [ $curr_count -lt $target_per_dev ]
do

	pv_name=`echo "osd.pv.$it"`
	dd if=/dev/zero of=$ECFAULT_HOME/img/${dev[curr]}/$pv_name bs=1M count=$target_sz
	#sleep 2
	let "curr=$it + $loop_idx" 
	losetup /dev/loop$(($it+$loop_idx)) $ECFAULT_HOME/img/${dev[curr]}/$pv_name
	sleep 1

	mkdir -p /sys/kernel/config/nvmet/subsystems/nvmet-$it \
	&& cd /sys/kernel/config/nvmet/subsystems/nvmet-$it
	echo 1 | tee -a attr_allow_any_host > /dev/null
	mkdir -p namespaces/$(($it+1)) && cd namespaces/$(($it+1))
	echo -n /dev/loop$(($it+$loop_idx)) | tee -a device_path > /dev/null
	echo 1 | tee -a enable > /dev/null
	sleep 1

	mkdir -p /sys/kernel/config/nvmet/ports/1 \
	&& cd /sys/kernel/config/nvmet/ports/1
	if [[ $it -eq 0 ]]; then
		echo ipv4 | tee -a addr_adrfam > /dev/null
		echo $conn | tee -a addr_trtype > /dev/null
		echo $addr_traddr | tee -a addr_traddr > /dev/null
		echo 4420 | tee -a addr_trsvcid > /dev/null
	fi
	$ECFAULT_HOME/symlink.py /sys/kernel/config/nvmet/subsystems/nvmet-$it /sys/kernel/config/nvmet/ports/1/subsystems/nvmet-$it
	sleep 1

	let  "it+=1"
       	let  "curr_count+=1"	

done

let "curr+=1"

done
sync

$ECFAULT_HOME/nvmetcli/nvmetcli save $ECFAULT_HOME/nvmet-config/$conn-$target_per_dev-$target_sz.json
