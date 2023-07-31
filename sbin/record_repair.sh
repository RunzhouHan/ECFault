#! /bin/bash

ceph osd pool repair ecpool
ceph osd pool force-recovery ecpool

for i in {1..2000}; 
do 
	date >> repair.bdwt ;
       	ceph osd pool stats >> repair.bdwt ;#| grep repair >> repair.bdwt; 
	sleep 2; 
done

cp repair.bdwt Q1/repair.bdwt-$(uuidgen)
rm repair.bdwt
