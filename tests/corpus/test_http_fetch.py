"""Retry timing checks with synthetic responses and no network traffic."""

import io
import unittest
from unittest import mock

from fadden import http_fetch


class HttpFetchTests(unittest.TestCase):
    def test_exhausted_attempts_sleep_only_between_requests(self):
        for tries in (0, 1, 3):
            for body in (b'{"error":"unavailable"}', b'not json', None):
                with self.subTest(tries=tries, body=body):
                    events = []

                    def request(*args, **kwargs):
                        events.append("request")
                        if body is None:
                            raise OSError("synthetic transport failure")
                        return io.BytesIO(body)

                    with mock.patch.object(http_fetch.urllib.request, "urlopen", request), \
                            mock.patch.object(http_fetch.time, "sleep", events.append):
                        result = http_fetch.fetch_json("https://example.invalid", tries=tries)
                    self.assertIsNone(result)
                    expected = [] if tries == 0 else ["request"] + [6, "request"] * (tries - 1)
                    self.assertEqual(events, expected)

    def test_success_after_failure_returns_without_another_sleep(self):
        events = []
        responses = iter((b'{"error":"unavailable"}', b'{"value":[]}'))

        def request(*args, **kwargs):
            events.append("request")
            return io.BytesIO(next(responses))

        with mock.patch.object(http_fetch.urllib.request, "urlopen", request), \
                mock.patch.object(http_fetch.time, "sleep", events.append):
            result = http_fetch.fetch_json("https://example.invalid")
        self.assertEqual(result, {"value": []})
        self.assertEqual(events, ["request", 6, "request"])
