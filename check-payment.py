from spaceremit.spaceremit_plugin import Spaceremit

all_accepted_tags = ["A", "B", "D", "E", "F"]
paid_tags = list(set(all_accepted_tags) - set(["F"]))

if 'SP_payment_code' in request.POST:
    payment_id = request.POST['SP_payment_code']
    acceptable_data = {
        "currency": "USD",
        "original_amount": 1,  # change to your amount
        "status_tag": all_accepted_tags  # SELECT NEEDED TAGS
    }

    spaceremit = Spaceremit()
    response = spaceremit.check_payment(payment_id, acceptable_data)
    if response:
        payment_details = spaceremit.data_return
        spaceremit_payment_id = payment_details['id']

        previous_payment_with_same_spaceremit_id = False
        if not previous_payment_with_same_spaceremit_id:

            # insert payment and save spaceremit_payment_id in your database

            if payment_details['status_tag'] in paid_tags:
                pass

        else:
            pass

    else:
        print(spaceremit.data_return)
