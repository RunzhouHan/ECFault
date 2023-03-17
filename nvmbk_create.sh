#!/bin/bash

# This script NVMe targets which can be connected with NVMe over TCP

modprobe nvme_tcp
modprobe nvmet
modprobe nvmet_tcp


me=$0
ECFAULT_HOME=$(cd -P -- `dirname $me`/ && pwd -P)

count=25 # number of OSDs
sz=6144 # OSD size
conn="tcp"
addr_traddr="192.168.1.7" # target host ip addr
it=0


while [ $it -lt $count ]
do

	pv_name=`echo "osd.pv.$it"`
	dd if=/dev/zero of=$ECFAULT_HOME/img/$pv_name bs=1M count=$sz
	sleep 2
	let "curr=$it + 20" # start from /dev/loop20, modify per your loop device availability
	losetup /dev/loop$(($it+20)) $ECFAULT_HOME/img/$pv_name
	sleep 1

	mkdir -p /sys/kernel/config/nvmet/subsystems/nvmet-$it \
	&& cd /sys/kernel/config/nvmet/subsystems/nvmet-$it
	echo 1 | tee -a attr_allow_any_host > /dev/null
	mkdir -p namespaces/$(($it+1)) && cd namespaces/$(($it+1))
	echo -n /dev/loop$(($it+20)) | tee -a device_path > /dev/null
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

done
sync


$ECFAULT_HOME/nvmetcli/nvmetcli save $ECFAULT_HOME/nvmet-config/$conn-$count-$sz.json