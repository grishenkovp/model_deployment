# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import predictions_pb2 as predictions__pb2


class PredictionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PredictIris = channel.unary_unary(
                '/Prediction/PredictIris',
                request_serializer=predictions__pb2.PredictRequest.SerializeToString,
                response_deserializer=predictions__pb2.PredictResponse.FromString,
                )


class PredictionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PredictIris(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PredictIris': grpc.unary_unary_rpc_method_handler(
                    servicer.PredictIris,
                    request_deserializer=predictions__pb2.PredictRequest.FromString,
                    response_serializer=predictions__pb2.PredictResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Prediction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Prediction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PredictIris(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Prediction/PredictIris',
            predictions__pb2.PredictRequest.SerializeToString,
            predictions__pb2.PredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
