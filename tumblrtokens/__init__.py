import oauth2
import urlparse


class Consumer:

    """
        Creates a new consumer for authentication with Tumblr.
    """

    def __init__(self, consumer_key, consumer_secret):

        return oauth2.Consumer(consumer_key, consumer_secret)


class RequestToken:

    """
        Creates a new request token for gaining credentials to authenticate with
         Tumblr.
    """

    def __init__(self, consumer):

        request_token_url = 'http://www.tumblr.com/oauth/request_token'

        client = oauth2.Client(consumer)

        resp, content = client.request(request_token_url, 'POST')

        self.token = urlparse.parse_qs(content)


class AccessToken:

    """
        Creates a new access token for gaining credentials to authenticate with
         Tumblr.
    """

    def __init__(self, consumer, request_response, request_token):

        access_token_url = 'http://www.tumblr.com/oauth/access_token'

        url = urlparse.urlparse(request_response)
        query_dict = urlparse.parse_qs(url.query)
        oauth_verifier = query_dict['oauth_verifier'][0]

        token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'][0])
        token.set_verifier(oauth_verifier)
        client = oauth2.Client(consumer)

        resp, content = client.request(access_token_url, 'POST')
        self.token = urlparse.parse_qs(content)