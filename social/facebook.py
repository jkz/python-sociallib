import callm
import authlib
import authlib.oauth2 as oauth2

class Error(Exception):
    pass


class ParseError(Error):
    pass


class Auth(authlib.Auth):
    def __call__(self, method, uri, body='', headers={}):
        """
        Add a token or id parameter to the query string.

        Heads up!

        Does not support duplicate keys.
        """

        resource = callm.Resource(uri)

        if self.token:
            resource.query['access_token'] = self.token.access_token
        elif self.app:
            resource.query['client_id'] = self.app.key

        return method, resource.uri, body, headers


class OAuth2(oauth2.API):
    secure = True
    host = 'graph.facebook.com'
    exchange_code_url = '/oauth/access_token'
    authenticate_uri = 'https://www.facebook.com/dialog/oauth'

    def auth_request(self, redirect_uri, state):
        return self.request_code(redirect_uri, state=state)

    def auth_callback(self, code, redirect_uri):
        response = self.exchange_code(code, redirect_uri)
        try:
            creds = response.query
        except ValueError:
            error = response.json
            raise Exception(error['type'] + error['message'])
        return self.auth.app.process_creds(**creds)


class API(callm.Connection):
    secure = True
    host = 'graph.facebook.com'
    exchange_code_url = '/oauth/access_token'
    authenticate_uri = 'https://www.facebook.com/dialog/oauth'

    def get_obj(self, uid, **options):
        return self.GET(uid, **options).json

    def get_status(self, uid):
        return self.get_obj(uid)

    def get_user(self, uid):
        fields = ['id', 'name', 'first_name', 'last_name', 'link', 'username',
                'gender', 'timezone', 'verified']
        return self.GET(uid, fields=fields).json

    def me(self):
        return self.get_user('me')

