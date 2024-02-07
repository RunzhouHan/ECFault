# ECFault
ECFault is a distributed virtualization-based fault injection framework for stress testing of erasure coding implementations in open-source distributed storage systems (DSS), for example, Ceph, HDFS, DAOS). 

## Introduction to ECFault ##
ECFault includes four major components: 

**ECFault Coordinator**:
[Coordinator](https://github.com/RunzhouHan/ECFault/blob/ECFault-v2.0/src/coordinator.py) manages the erasure coding configurations of the DSS and sends out control requests to ECFault workers for EC-oriented DSS manipulation. A submodule named EC Manager controls the EC-related configurations in DSS. For example, in case of Ceph, the EC manager can precisely create a erasure-coded pool with desired specifications including EC plugin (e.g., Jerasure), EC parameters (e.g., 𝑘 and 𝑚), chunk size, etc. Besides EC-specific configurations, it also controls other relevant system features that may affect the EC op- erations, such as the number of placement groups in the erasure-coded pool (i.e., pg_num). 

**ECFault Worker**:
[Workers](https://github.com/RunzhouHan/ECFault/blob/ECFault-v2.0/src/worker.py) listen to requests from [Coordinator](https://github.com/RunzhouHan/ECFault/blob/ECFault-v2.0/src/coordinator.py) to finish two major jobs:
(1) Virtual disk provisioning to the DSS storage servers, which decouples the storage devices from the target DSS servers to allow easy control of storage states;
(2) DSS manipulation, which includes a set of submodules to inject a variety of faults to trigger the EC operations in the target DSS under different workloads and configurations. ECFault Worker currently supports following types of failures:
  - Node failure
  - Device failure
  - Block failure

**Monitor**:
[Monitor](https://github.com/RunzhouHan/ECFault/tree/ECFault-v2.0/src/kafka) is co-located with the metadata node containing system information (e.g., system topology, object map, erasure code parameters) of the cluster. It collects disk I/O and network traffic statistics and send them to [Coordinator](https://github.com/RunzhouHan/ECFault/blob/ECFault-v2.0/src/coordinator.py) through Kakfa to analysis erasure coding’s performance.

**Workload**:
[Workload](https://github.com/RunzhouHan/ECFault/tree/ECFault-v2.0/sbin) includes a series of configurable I/O workloads for three Ceph interfaces:
  - RADOS
  - RBD
  - CephFS

## ECFault Initiation Guidance ##

Steps to initiate the tool：

  1.  (Optional) Required to be able to run sudo commands

  2.  Install dependencies:
      ```
      sudo apt install nvme-cli configshell-fb nvmetcli
      sudo apt install -y protobuf-compiler
      pip install kafka-python
      pip install iostat-tool
      pip install grpcio
      ```
      
  3.  Create a virtual NVMe device
      ```
      ./nvmebk_create.sh
      ```

  4.  Connect to the virtual NVMe device on target operating system:
      ```
      modprobe nvme-fabrics
      nvme discover -t tcp -a <ip_address> -s 4420
      nvme connect -t tcp -n nvmet-0 -a <ip_address> -s 4420
      ```
  
  5.  Create a DSS cluster using virtual disks as usual

  6.  Inject a fault to the DSS with ECFault worker:
      ```
      python /src/worker.py
      ```
  7.  Observe erasure coding recovery process in DSS
     
  8.  Clean up virtual NVMe devices:
      ```
      ./nvmebk_remove.sh
      ```  





