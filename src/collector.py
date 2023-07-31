import logging

import grpc
import ecfault_pb2
import ecfault_pb2_grpc



channel = grpc.insecure_channel('localhost:50051')
remote_nvme_dev_stub = ecfault_pb2_grpc.RemoteNVMeDevStub(channel)
fault_injection_stub = ecfault_pb2_grpc.FaultInjectionStub(channel)

ph = ecfault_pb2.Placeholder(op = 0)
message = remote_nvme_dev_stub.get_avail_dev(ph)
print(message)

vdi = ecfault_pb2.VirtDevInfo(dev_path = "/",
	bk_path = "/",
	bk_per_dev = 1,
	bk_sz = 1024)

message = remote_nvme_dev_stub.nvme_dev_create(vdi)
print(message)

vdim = ecfault_pb2.VirtDevInfoMultiple(dev_path = ["/"],
	bk_path = "/",
	bk_per_dev = 1,
	bk_sz = 1024)
message = remote_nvme_dev_stub.nvme_dev_create_multiple(vdim)
print(message)

message = remote_nvme_dev_stub.nvme_dev_remove(ph)
print(message)

fault = ecfault_pb2.Fault(fault = 0)
message = fault_injection_stub.inject_fault(fault)
print(message)