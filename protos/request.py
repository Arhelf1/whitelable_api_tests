from protos.access_api_pb2 import RegistrationRequest, ConfirmRegistrationRequest


class Request(object):

    @staticmethod
    def req_reg(reg):
        return RegistrationRequest(phone=reg["phone"],
                                   email=reg["email"],
                                   password=reg["password"])

    @staticmethod
    def req_confirm(user_id):
        return ConfirmRegistrationRequest(user_id=user_id, code="000000")
