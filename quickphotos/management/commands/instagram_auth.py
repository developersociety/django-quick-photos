from django.core.management.base import BaseCommand
from django.utils.six.moves import input
from instagram.client import InstagramAPI


def get_auth_tokens(stdout):
    stdout.write('Please enter the following Instagram client details\n\n')
    client_id = input('Client ID: ').strip()
    client_secret = input('Client Secret: ').strip()
    redirect_uri = input('Redirect URI: ').strip()
    raw_scope = input(
        'Requested scope (separated by spaces, blank for just basic read): ').strip()
    scope = raw_scope.split(' ')

    # For basic, API seems to need to be set explicitly
    if not scope or scope == ['']:
        scope = ['basic']

    api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    redirect_uri = api.get_authorize_login_url(scope=scope)

    stdout.write('\nVisit this page and authorize access in your browser:\n\n%s\n\n' % redirect_uri)

    code = input('Paste in code in query string after redirect: ').strip()

    access_token = api.exchange_code_for_access_token(code)
    stdout.write('Access token:\n\n%s\n\n' % (access_token,))


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_auth_tokens(self.stdout)
