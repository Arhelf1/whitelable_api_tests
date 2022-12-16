auth_headers = {
        'Content-Type': 'application/json'
}
data = "{\n    \"password\": \"Vfhn2019\",\n    \"device\": {\n                \"local_id\": \"QADevice\",\n                \"name\": \"CurlDevice\",\n                \"info\": {\n                          \"0\": \"testing\",\n                          \"26\": \"testing\"\n                        }               \n              }\n}\n"
url_refresh = "http://wl-ka-integration-test-shared.entapp.work/Token/CreateRefresh?globalId=EC799AE2-3C39-4225-93BD-5D8BDB0D6BD7"
url_refresh_finam2 = 'http://wl-ka-integration-test-shared.entapp.work/Token/CreateRefresh?globalId=CB176865-D136-42FE-8D7E-B0AB30FCF399'
full_url_access = 'http://wl-test-shared.entapp.work/v1/PartnerAuth/RefreshToken'
short_url_access = 'PartnerAuth/RefreshToken'