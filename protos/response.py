class Response(object):

    @staticmethod
    def resp_reg(request, stub):
        resp = stub.Register(request)
        return resp

    @staticmethod
    def resp_confirm(request, stub):
        return stub.ConfirmRegistration(request)
