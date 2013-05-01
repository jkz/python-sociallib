import unittest

from sociallib import youtube

KEY = '710512928255-pc72ripnl3uddvjbbhleb19oii6s34dd.apps.googleusercontent.com'
SECRET = 'l6dHjd758prrb6tMH9lc4bEw'
REDIRECT = 'http://dev.jessethegame.net/youtube/acua/connect/callback/'

class TestCase(unittest.TestCase):
    def test(self):
        consumer = youtube.Consumer(KEY, SECRET)
        auth = youtube.Auth(consumer=consumer)
        provider = youtube.Provider(auth=auth)
        url = provider.request_code(REDIRECT)

        expected_url = 'https://accounts.google.com/o/oauth2/auth?redirect_uri=http%3A%2F%2Fdev.jessethegame.net%2Fyoutube%2Facua%2Fconnect%2Fcallback%2F&response_type=code&client_id=710512928255-pc72ripnl3uddvjbbhleb19oii6s34dd.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube&approval_prompt=auto&access_type=offline'

        self.assertEqual(url, expected_url)

