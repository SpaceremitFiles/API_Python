from spaceremit.spaceremit_plugin import Spaceremit

if request.method == 'POST':
    json_data = request.data.decode('utf-8')
    request_data = json.loads(json_data)
    
    if request_data is not None:
        SPACEREMIT_PAYMENT_ID = request_data['data']['id']
        
        acceptable_data = {}
        spaceremit = Spaceremit()
        response = spaceremit.check_payment(SPACEREMIT_PAYMENT_ID, acceptable_data)
        if response:
            SPACEREMIT_PAYMENT_DATA = spaceremit.data_return
            newStatus = SPACEREMIT_PAYMENT_DATA['status_tag']
            oldStatus = "B"

            """
            switch newStatus:
                case 'A':
                    if oldStatus == 'B':
                        pass
                    if oldStatus == 'C':
                        pass
                    break
                case 'B':
                    if oldStatus == 'A':
                        pass
                    if oldStatus == 'C':
                        pass
                    break
                default:
                    break
            """
        else:
            pass
    else:
        pass
else:
    pass
