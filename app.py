from flask import Flask, render_template, request
from spaceremit.spaceremit_plugin import Spaceremit

app = Flask(__name__)

all_accepted_tags = ["A", "B", "D", "E", "F"]
paid_tags = list(set(all_accepted_tags) - set(["F"]))

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        spaceremit = Spaceremit()
        payment_id = request.form['SP_payment_code']
        acceptable_data = {
            "currency": "USD",
            "original_amount": 1,  # change to your amount
            "status_tag": all_accepted_tags  # SELECT NEEDED TAGS
        }

        response = spaceremit.check_payment(payment_id, acceptable_data)
        if response:
            payment_details = spaceremit.data_return
            spaceremit_payment_id = payment_details['id']

            previous_payment_with_same_spaceremit_id = False
            if not previous_payment_with_same_spaceremit_id:
                if payment_details['status_tag'] in paid_tags:
                    pass  # Perform action for successful payment
                    
                return 'Payment processed successfully'  # Placeholder response, replace with actual processing logic

            else:
                return 'Payment was inserted previously. Only show message to user that payment is completed or pending, nothing else.'

        else:
            return spaceremit.data_return

    else:
        return render_template('main_page.html')

if __name__ == '__main__':
    app.run(debug=True)
