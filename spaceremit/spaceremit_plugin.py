import requests

class Spaceremit:
    SERVER_KEY = 'YOUR_PRIVATE_KEY'
    BASE_URL = 'https://spaceremit.com/api/v2/payment_info/'

    def __init__(self):
        self.data_return = None

    def send_api_request(self, data, request_method=None):
        func_return = False
        data['private_key'] = self.SERVER_KEY
        headers = {'authorization': self.SERVER_KEY, 'Content-Type': 'application/json'}
        try:
            response = requests.post(self.BASE_URL, json=data, headers=headers)
            if response.status_code == 200:
                decoded_response = response.json()
                self.data_return = decoded_response
                func_return = True
            else:
                self.data_return = {'response_status': 'failed',
                                    'message': 'Failed to connect to spaceremit with status code ' + str(response.status_code)}
        except Exception as e:
            self.data_return = {'response_status': 'failed',
                                'message': 'Failed to connect to spaceremit: ' + str(e)}
        return func_return

    def check_payment(self, payment_id, acceptable_data):
        func_return = False
        spaceremit = Spaceremit()
        data = {'payment_id': payment_id}
        response = spaceremit.send_api_request(data)
        if response:
            response_data = spaceremit.data_return.get('data', {})
            if spaceremit.data_return.get('response_status') == 'success':
                not_acceptable_data_found = False
                not_acceptable_data_value = None
                for accept_k, accept_v in acceptable_data.items():
                    if accept_k == 'status_tag':
                        if response_data.get('status_tag') not in accept_v:
                            not_acceptable_data_found = True
                            not_acceptable_data_value = response_data.get('status_tag')
                            break
                    elif acceptable_data[accept_k] != response_data.get(accept_k):
                        not_acceptable_data_found = True
                        not_acceptable_data_value = response_data.get(accept_k)
                        break
                if not_acceptable_data_found:
                    self.data_return = "Not acceptable value is (" + str(not_acceptable_data_value) + ")"
                else:
                    func_return = True
                    self.data_return = response_data
            else:
                self.data_return = response["message"]
        else:
            self.data_return = spaceremit.data_return["message"]
        return func_return
