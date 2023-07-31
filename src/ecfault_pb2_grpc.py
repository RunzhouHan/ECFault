# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ecfault_pb2 as ecfault__pb2


class RemoteNVMeDevStub(object):
    """virtual nvme device management 

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_avail_dev = channel.unary_unary(
                '/ecfault.RemoteNVMeDev/get_avail_dev',
                request_serializer=ecfault__pb2.Placeholder.SerializeToString,
                response_deserializer=ecfault__pb2.DevInfo.FromString,
                )
        self.nvme_dev_create = channel.unary_unary(
                '/ecfault.RemoteNVMeDev/nvme_dev_create',
                request_serializer=ecfault__pb2.VirtDevInfo.SerializeToString,
                response_deserializer=ecfault__pb2.Stat.FromString,
                )
        self.nvme_dev_create_multiple = channel.unary_unary(
                '/ecfault.RemoteNVMeDev/nvme_dev_create_multiple',
                request_serializer=ecfault__pb2.VirtDevInfoMultiple.SerializeToString,
                response_deserializer=ecfault__pb2.Stat.FromString,
                )
        self.nvme_dev_remove = channel.unary_unary(
                '/ecfault.RemoteNVMeDev/nvme_dev_remove',
                request_serializer=ecfault__pb2.Placeholder.SerializeToString,
                response_deserializer=ecfault__pb2.Stat.FromString,
                )


class RemoteNVMeDevServicer(object):
    """virtual nvme device management 

    """

    def get_avail_dev(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def nvme_dev_create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def nvme_dev_create_multiple(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def nvme_dev_remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteNVMeDevServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_avail_dev': grpc.unary_unary_rpc_method_handler(
                    servicer.get_avail_dev,
                    request_deserializer=ecfault__pb2.Placeholder.FromString,
                    response_serializer=ecfault__pb2.DevInfo.SerializeToString,
            ),
            'nvme_dev_create': grpc.unary_unary_rpc_method_handler(
                    servicer.nvme_dev_create,
                    request_deserializer=ecfault__pb2.VirtDevInfo.FromString,
                    response_serializer=ecfault__pb2.Stat.SerializeToString,
            ),
            'nvme_dev_create_multiple': grpc.unary_unary_rpc_method_handler(
                    servicer.nvme_dev_create_multiple,
                    request_deserializer=ecfault__pb2.VirtDevInfoMultiple.FromString,
                    response_serializer=ecfault__pb2.Stat.SerializeToString,
            ),
            'nvme_dev_remove': grpc.unary_unary_rpc_method_handler(
                    servicer.nvme_dev_remove,
                    request_deserializer=ecfault__pb2.Placeholder.FromString,
                    response_serializer=ecfault__pb2.Stat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecfault.RemoteNVMeDev', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoteNVMeDev(object):
    """virtual nvme device management 

    """

    @staticmethod
    def get_avail_dev(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecfault.RemoteNVMeDev/get_avail_dev',
            ecfault__pb2.Placeholder.SerializeToString,
            ecfault__pb2.DevInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def nvme_dev_create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecfault.RemoteNVMeDev/nvme_dev_create',
            ecfault__pb2.VirtDevInfo.SerializeToString,
            ecfault__pb2.Stat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def nvme_dev_create_multiple(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecfault.RemoteNVMeDev/nvme_dev_create_multiple',
            ecfault__pb2.VirtDevInfoMultiple.SerializeToString,
            ecfault__pb2.Stat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def nvme_dev_remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecfault.RemoteNVMeDev/nvme_dev_remove',
            ecfault__pb2.Placeholder.SerializeToString,
            ecfault__pb2.Stat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StatQueryStub(object):
    """query stats 

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.system_stats_query = channel.unary_unary(
                '/ecfault.StatQuery/system_stats_query',
                request_serializer=ecfault__pb2.Placeholder.SerializeToString,
                response_deserializer=ecfault__pb2.SystemStats.FromString,
                )
        self.node_stats_query = channel.unary_unary(
                '/ecfault.StatQuery/node_stats_query',
                request_serializer=ecfault__pb2.Placeholder.SerializeToString,
                response_deserializer=ecfault__pb2.NodeStats.FromString,
                )


class StatQueryServicer(object):
    """query stats 

    """

    def system_stats_query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def node_stats_query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatQueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'system_stats_query': grpc.unary_unary_rpc_method_handler(
                    servicer.system_stats_query,
                    request_deserializer=ecfault__pb2.Placeholder.FromString,
                    response_serializer=ecfault__pb2.SystemStats.SerializeToString,
            ),
            'node_stats_query': grpc.unary_unary_rpc_method_handler(
                    servicer.node_stats_query,
                    request_deserializer=ecfault__pb2.Placeholder.FromString,
                    response_serializer=ecfault__pb2.NodeStats.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecfault.StatQuery', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StatQuery(object):
    """query stats 

    """

    @staticmethod
    def system_stats_query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecfault.StatQuery/system_stats_query',
            ecfault__pb2.Placeholder.SerializeToString,
            ecfault__pb2.SystemStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def node_stats_query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecfault.StatQuery/node_stats_query',
            ecfault__pb2.Placeholder.SerializeToString,
            ecfault__pb2.NodeStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FaultInjectionStub(object):
    """fault injection 

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.inject_fault = channel.unary_unary(
                '/ecfault.FaultInjection/inject_fault',
                request_serializer=ecfault__pb2.Fault.SerializeToString,
                response_deserializer=ecfault__pb2.Stat.FromString,
                )


class FaultInjectionServicer(object):
    """fault injection 

    """

    def inject_fault(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FaultInjectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'inject_fault': grpc.unary_unary_rpc_method_handler(
                    servicer.inject_fault,
                    request_deserializer=ecfault__pb2.Fault.FromString,
                    response_serializer=ecfault__pb2.Stat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecfault.FaultInjection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FaultInjection(object):
    """fault injection 

    """

    @staticmethod
    def inject_fault(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecfault.FaultInjection/inject_fault',
            ecfault__pb2.Fault.SerializeToString,
            ecfault__pb2.Stat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)