from Letskucoin.account.models import User, Position
from kucoin.client import User as U


def check_information():
    users = User.objects.all()
    print("Checking information....")
    for user in users:
        try:
            client = U(user.api_key, user.api_secret, user.api_passphrase)
            resp = client.get_account_list()[0]
            print(resp)
            Position.objects.create(user_id=user.id, id=resp['id'], currency=resp['currency'],
                                    account_type=resp['type'],
                                    balance=resp['balance'], available=resp['available'], holds=resp['holds'])

        except Exception as e:
            print(e)
