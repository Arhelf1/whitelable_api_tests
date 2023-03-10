# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import access_api_pb2 as grpc_dot_edox_dot_access_dot_access__api__pb2


class AccessApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetRegistrationInfo = channel.unary_unary(
        '/grpc.edox.access.AccessApi/GetRegistrationInfo',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.GetRegistrationInfoRequest.SerializeToString,
        response_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RegistrationInfo.FromString,
        )
    self.RequestRestoreAccess = channel.unary_unary(
        '/grpc.edox.access.AccessApi/RequestRestoreAccess',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RequestRestoreAccessRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CheckRestoreAccess = channel.unary_unary(
        '/grpc.edox.access.AccessApi/CheckRestoreAccess',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckRestoreAccessRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ConfirmRestoreAccess = channel.unary_unary(
        '/grpc.edox.access.AccessApi/ConfirmRestoreAccess',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmRestoreAccessRequest.SerializeToString,
        response_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmRestoreAccessResponse.FromString,
        )
    self.RestoreAccess = channel.unary_unary(
        '/grpc.edox.access.AccessApi/RestoreAccess',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RestoreAccessRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CheckRegistration = channel.unary_unary(
        '/grpc.edox.access.AccessApi/CheckRegistration',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckRegistrationRequest.SerializeToString,
        response_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckRegistrationResponse.FromString,
        )
    self.Register = channel.unary_unary(
        '/grpc.edox.access.AccessApi/Register',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RegistrationRequest.SerializeToString,
        response_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RegistrationResponse.FromString,
        )
    self.ConfirmRegistration = channel.unary_unary(
        '/grpc.edox.access.AccessApi/ConfirmRegistration',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmRegistrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RenewRegistrationConfirmation = channel.unary_unary(
        '/grpc.edox.access.AccessApi/RenewRegistrationConfirmation',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RenewRegistrationConfirmationRequest.SerializeToString,
        response_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RenewRegistrationConfirmationResponse.FromString,
        )
    self.RequestEmailConfirmation = channel.unary_unary(
        '/grpc.edox.access.AccessApi/RequestEmailConfirmation',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RequestEmailConfirmationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ConfirmEmail = channel.unary_unary(
        '/grpc.edox.access.AccessApi/ConfirmEmail',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmEmailRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ChangeLogin = channel.unary_unary(
        '/grpc.edox.access.AccessApi/ChangeLogin',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ChangeLoginRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CheckLoginInUse = channel.unary_unary(
        '/grpc.edox.access.AccessApi/CheckLoginInUse',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckLoginInUseRequest.SerializeToString,
        response_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckLoginInUseResponse.FromString,
        )
    self.ChangePassword = channel.unary_unary(
        '/grpc.edox.access.AccessApi/ChangePassword',
        request_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ChangePasswordRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AccessApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetRegistrationInfo(self, request, context):
    """???????????????? ?????????????????????? ???????????????????????? 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RequestRestoreAccess(self, request, context):
    """???????????? ???????????????????????????? ?????????????? 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckRestoreAccess(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfirmRestoreAccess(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreAccess(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckRegistration(self, request, context):
    """?????????????????????? 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfirmRegistration(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RenewRegistrationConfirmation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RequestEmailConfirmation(self, request, context):
    """???????????????????? ???????????? ???????????????????????? ?????? ?????????????????????????? ?????????? 
    JWT-Authentication    
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConfirmEmail(self, request, context):
    """?????????? ?????????????????????????? ??????????
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangeLogin(self, request, context):
    """?????????? ?????????? ????????????
    JWT-Authentication   
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckLoginInUse(self, request, context):
    """?????????? ???????????????? ?????????????????? ????????????
    JWT-Authentication   
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangePassword(self, request, context):
    """?????????? ?????????? ????????????
    JWT-Authentication 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccessApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetRegistrationInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetRegistrationInfo,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.GetRegistrationInfoRequest.FromString,
          response_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RegistrationInfo.SerializeToString,
      ),
      'RequestRestoreAccess': grpc.unary_unary_rpc_method_handler(
          servicer.RequestRestoreAccess,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RequestRestoreAccessRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CheckRestoreAccess': grpc.unary_unary_rpc_method_handler(
          servicer.CheckRestoreAccess,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckRestoreAccessRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ConfirmRestoreAccess': grpc.unary_unary_rpc_method_handler(
          servicer.ConfirmRestoreAccess,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmRestoreAccessRequest.FromString,
          response_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmRestoreAccessResponse.SerializeToString,
      ),
      'RestoreAccess': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreAccess,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RestoreAccessRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CheckRegistration': grpc.unary_unary_rpc_method_handler(
          servicer.CheckRegistration,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckRegistrationRequest.FromString,
          response_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckRegistrationResponse.SerializeToString,
      ),
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RegistrationRequest.FromString,
          response_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RegistrationResponse.SerializeToString,
      ),
      'ConfirmRegistration': grpc.unary_unary_rpc_method_handler(
          servicer.ConfirmRegistration,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmRegistrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RenewRegistrationConfirmation': grpc.unary_unary_rpc_method_handler(
          servicer.RenewRegistrationConfirmation,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RenewRegistrationConfirmationRequest.FromString,
          response_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RenewRegistrationConfirmationResponse.SerializeToString,
      ),
      'RequestEmailConfirmation': grpc.unary_unary_rpc_method_handler(
          servicer.RequestEmailConfirmation,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.RequestEmailConfirmationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ConfirmEmail': grpc.unary_unary_rpc_method_handler(
          servicer.ConfirmEmail,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ConfirmEmailRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ChangeLogin': grpc.unary_unary_rpc_method_handler(
          servicer.ChangeLogin,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ChangeLoginRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CheckLoginInUse': grpc.unary_unary_rpc_method_handler(
          servicer.CheckLoginInUse,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckLoginInUseRequest.FromString,
          response_serializer=grpc_dot_edox_dot_access_dot_access__api__pb2.CheckLoginInUseResponse.SerializeToString,
      ),
      'ChangePassword': grpc.unary_unary_rpc_method_handler(
          servicer.ChangePassword,
          request_deserializer=grpc_dot_edox_dot_access_dot_access__api__pb2.ChangePasswordRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.edox.access.AccessApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
