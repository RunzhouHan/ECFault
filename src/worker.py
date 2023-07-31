from concurrent import futures
import logging

import grpc
import ecfault_pb2
import ecfault_pb2_grpc
import subprocess

class RemoteNVMeDevServicer(ecfault_pb2_grpc.RemoteNVMeDevServicer):
	def get_avail_dev(self, request, context):
		cmd = "nvme list"
		info = subprocess.call(cmd, shell=True)
		return ecfault_pb2.DevInfo(dev_info = cmd)

	def nvme_dev_create(self, request, context):
		return ecfault_pb2.Stat(stat = 0)
		# return ecfault_pb2.DevInfo(dev_info = "nvme_dev_create")

	def nvme_dev_create_multiple(self, request, context):
		# return ecfault_pb2.Stat(stat = 0)
		return ecfault_pb2.DevInfo(dev_info = "nvme_dev_create_multiple")

	def nvme_dev_remove(self, request, context):
		# return ecfault_pb2.Stat(stat = 0)
		return ecfault_pb2.DevInfo(dev_info = "nvme_dev_remove")


class FaultInjectionServicer(ecfault_pb2_grpc.FaultInjectionServicer):
	def inject_fault(self, request, context):
		# return ecfault_pb2.Stat(stat = 0)
		return ecfault_pb2.DevInfo(dev_info = "inject_fault")



def worker_run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ecfault_pb2_grpc.add_RemoteNVMeDevServicer_to_server(RemoteNVMeDevServicer(), server)
    ecfault_pb2_grpc.add_FaultInjectionServicer_to_server(FaultInjectionServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("server start")
    server.start()
    print("server started")
    server.wait_for_termination()
    print("server term")


if __name__ == "__main__":
	logging.basicConfig()
	worker_run()