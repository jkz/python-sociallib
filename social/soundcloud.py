import callm
import authlib
import authlib.oauth2 as oauth2

class Error(Exception):
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
            resource.query['oauth_token'] = self.token.access_token
        elif self.app:
            resource.query['client_id'] = self.app.key

        return method, resource.uri, body, headers


class API(oauth2.API):
    secure = True
    host = 'api.soundcloud.com'
    exchange_code_url = '/oauth2/token'
    authenticate_uri = 'https://soundcloud.com/connect'

    format = 'json'

    def me(self):
        return self.GET('/me.json')

    def get_my_tracks(self):
        return self.GET('/me/tracks.json')

    def get_user(self, uid):
        return self.GET('/users/%s.json' % uid)

    def get_user_tracks(self, uid):
        return self.GET('/users/%s/tracks.json' % uid)

    def get_track(self, uid):
        return self.GET('/tracks/%s.json' % uid)

