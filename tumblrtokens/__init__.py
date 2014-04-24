import oauth2
import urlparse


def consumer(consumer_key, consumer_secret):

    """
        Creates a new consumer for authentication with Tumblr.
    """

    return oauth2.Consumer(consumer_key, consumer_secret)


def request_token(consumer):

    """
        Creates a new request token for gaining credentials to authenticate with
         Tumblr.
    """

    request_token_url = 'http://www.tumblr.com/oauth/request_token'

    client = oauth2.Client(consumer)

    resp, content = client.request(request_token_url, 'POST')

    return urlparse.parse_qs(content)


def access_token(consumer, request_response, request_token):

    """
        Creates a new access token for gaining credentials to authenticate with
         Tumblr.
    """

    access_token_url = 'http://www.tumblr.com/oauth/access_token'

    url = urlparse.urlparse(request_response)
    query_dict = urlparse.parse_qs(url.query)
    oauth_verifier = query_dict['oauth_verifier'][0]

    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'][0])
    token.set_verifier(oauth_verifier)
    client = oauth2.Client(consumer, token)

    resp, content = client.request(access_token_url, 'POST')
    return urlparse.parse_qs(content)