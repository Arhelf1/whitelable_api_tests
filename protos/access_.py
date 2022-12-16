from protos.request import Request
from protos.response import Response


class Access(Request, Response):

    def registration(self, data, stub):
        return self.resp_reg(self.req_reg(data), stub)

    def confirm(self, user_id, stub):
        return self.resp_confirm(self.req_confirm(user_id), stub)

