import unittest
from unittest import mock
import json

from smartdiffer.diffchecker import API_ENDPOINT, WEB_URL
from smartdiffer.diffchecker import get_diff_url


def mocked_requests_post(*args, **kwargs):
    class MockDiffcheckerResponse:
        def __init__(self, text):
            if text:
                self.text = text

    url = kwargs.get('url')
    data = kwargs.get('json')

    if url == API_ENDPOINT + '/diffs' and 'invalid' not in data.get('Authorization'):
        print(data.get('Authorization'))
        slug = build_slug(data.get('left'), data.get('right'))
        text = json.dumps({'slug': slug})
        return MockDiffcheckerResponse(text)
    return MockDiffcheckerResponse(None)


def mocked_diffchecker_auth_token(token):
    return lambda: token


def build_slug(left, right):
    # for testing purposes
    return str(hash(str(left) + str(right)))


class TestGetDiffUrl(unittest.TestCase):
    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_success(self, mock_post):
        left = 'A123'
        right = 'B234'
        url = get_diff_url(left, right)
        slug = build_slug(left, right)
        self.assertEqual(url, WEB_URL + slug)

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    @mock.patch('smartdiffer.diffchecker.API_ENDPOINT', 'another endpoint')
    def test_invalid_endpoint(self, mock_post):
        left = 'A123'
        right = 'B234'
        self.assertRaises(AttributeError, get_diff_url, *(left, right))

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    @mock.patch('smartdiffer.diffchecker.get_diffchecker_auth_token',
                side_effect=mocked_diffchecker_auth_token('invalid'))
    def test_invalid_invalid_auth_token(self, mock_post, mock_token):
        left = 'A123'
        right = 'B234'
        self.assertRaises(AttributeError, get_diff_url, *(left, right))


if __name__ == '__main__':
    unittest.main()
