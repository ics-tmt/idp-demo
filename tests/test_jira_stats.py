import unittest
from unittest.mock import patch, Mock

from jira_api.jira_stats import get_story_ticket_counts


class TestGetStoryTicketCounts(unittest.TestCase):
    @patch('jira_api.jira_stats.requests.get')
    def test_single_page(self, mock_get):
        mock_resp = Mock()
        mock_resp.json.return_value = {
            'issues': [
                {'fields': {'issuetype': {'name': 'Story'}}},
                {'fields': {'issuetype': {'name': 'Bug'}}},
                {'fields': {'issuetype': {'name': 'Story'}}},
            ],
            'total': 3
        }
        mock_resp.raise_for_status = Mock()
        mock_get.return_value = mock_resp

        counts = get_story_ticket_counts('http://jira', 'PROJ', ('user', 'token'))
        self.assertEqual(counts, {'Story': 2, 'Bug': 1})

    @patch('jira_api.jira_stats.requests.get')
    def test_multiple_pages(self, mock_get):
        total = 3
        page1 = {'issues': [
            {'fields': {'issuetype': {'name': 'Story'}}},
        ], 'total': total}
        page2 = {'issues': [
            {'fields': {'issuetype': {'name': 'Bug'}}},
            {'fields': {'issuetype': {'name': 'Bug'}}},
        ], 'total': total}

        resp1 = Mock()
        resp1.json.return_value = page1
        resp1.raise_for_status = Mock()
        resp2 = Mock()
        resp2.json.return_value = page2
        resp2.raise_for_status = Mock()
        mock_get.side_effect = [resp1, resp2]

        counts = get_story_ticket_counts('http://jira', 'PROJ', ('user', 'token'))
        self.assertEqual(counts, {'Story': 1, 'Bug': 2})


if __name__ == '__main__':
    unittest.main()
