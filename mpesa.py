import base64
import requests

def get_access_token():
    consumer_key = '3rExRUVFEjP4ShJAnGprsFjh1Cwypdx8EWzsNLtqRf80C0dc'
    consumer_secret = 'hy3dcxyki38V7oY4AxODFE5fYLlwoGu7a9lK8EuV9XgqMkGJyChMfBRGwxwQCaE7'
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    # Encode the Consumer Key and Secret in Base64
    auth = base64.b64encode(f'{consumer_key}:{consumer_secret}'.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': f'Basic {auth}'
    }

    # Get the token from Safaricom
    response = requests.get(api_url, headers=headers)
    json_response = response.json()
    access_token = json_response['access_token']
    return access_token


def lipa_na_mpesa(amount, phone_number):
    access_token = get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    lipa_na_mpesa_online_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    payload = {
        'BusinessShortcode': '174379',  # Use the sandbox shortcode (replace with actual once live)
        'LipaNaMpesaOnlineShortcode': '174379',  # Use the sandbox shortcode (replace with actual once live)
        'LipaNaMpesaOnlineShortcodePassword': 'your_shortcode_password',  # Use the password for your shortcode
        'PhoneNumber': phone_number,  # M-Pesa phone number to make the payment
        'Amount': amount,  # Amount to pay
        'AccountReference': 'EduBridge Donation',  # Payment description
        'TransactionDesc': 'Payment for Education',  # Transaction description
    }

    response = requests.post(lipa_na_mpesa_online_url, json=payload, headers=headers)
    return response.json()
