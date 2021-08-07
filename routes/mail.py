  
# For SMTP
from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from config import mail_config



@app.route('/share', methods=['POST'])
def shareCredential():
    
    try:
        _email = request.form('email')
        _name = request.form('name')
        _credential = request.form('credential')
        print("Sending Invoice Mail")


        # create an instance of the API class
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(mail_config))
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{
                "email": _email,
                "name": _name}],
            template_id=3,
            params=_credential,
            headers={
                "X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3",
                "charset": "iso-8859-1"
            }
        )  # SendSmtpEmail | Values to send a transactional email

        # Send a transactional email
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)

    except ApiException as e:
        raise("Send In Blue Error", f"Exception when calling SMTPApi->send_transac_email: {e}\n")
    
