import os
import unittest

from unittest.mock import patch
from fastapi import HTTPException

from backend import jira_client
from backend.app import story_ticket_count


class DummyResponse:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self._data = data

    def json(self):
        return self._data


class JiraClientTest(unittest.TestCase):
    @patch.dict('os.environ', {
        'JIRA_BASE_URL': 'https://example.atlassian.net',
        'JIRA_USERNAME': 'user',
        'JIRA_TOKEN': 'token',
        'JIRA_PROJECT_KEY': 'TEST',
    })
    @patch('backend.jira_client.requests.get')
    def test_get_story_ticket_counts(self, mock_get):
        sample_api_response = {
            "total": 2,
            "issues": [
                {"key": "TEST-1", "fields": {"summary": "First story", "subtasks": [{}, {}]}},
                {"key": "TEST-2", "fields": {"summary": "Second story", "subtasks": []}},
            ],
        }
        mock_get.return_value = DummyResponse(200, sample_api_response)
        result = jira_client.get_story_ticket_counts()
        expected = [
            {"key": "TEST-1", "summary": "First story", "ticket_count": 2},
            {"key": "TEST-2", "summary": "Second story", "ticket_count": 0},
        ]
        self.assertEqual(result, expected)


class ApiEndpointTest(unittest.TestCase):
    @patch('backend.app.get_story_ticket_counts')
    def test_story_ticket_count_success(self, mock_counts):
        sample_data = [{"key": "TEST-1", "summary": "First story", "ticket_count": 2}]
        mock_counts.return_value = sample_data
        result = story_ticket_count()
        self.assertEqual(result, sample_data)

    @patch('backend.app.get_story_ticket_counts')
    def test_story_ticket_count_error(self, mock_counts):
        mock_counts.side_effect = jira_client.JiraClientError('config missing')
        with self.assertRaises(HTTPException) as ctx:
            story_ticket_count()
        self.assertEqual(ctx.exception.status_code, 500)
        self.assertEqual(ctx.exception.detail, 'config missing')


if __name__ == '__main__':
    unittest.main()
