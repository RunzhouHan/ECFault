#!/bin/bash

me=$0
ECFAULT_HOME=$(cd -P -- `dirname $me`/ && pwd -P)
count=$(ls -1q $ECFAULT_HOME/img | wc -l)
echo 
it=0

$ECFAULT_HOME/nvmetcli/nvmetcli clear

while [ $it -lt $count ]
do

pv_name=`echo "osd.pv.$it"`
let "curr=$it + 20"
losetup -d /dev/loop$curr
let  "it+=1" 

done
sync

rm -f $ECFAULT_HOME/img/*

echo "Removed $count nvme targets"