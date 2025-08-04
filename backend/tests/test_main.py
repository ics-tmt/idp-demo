import unittest
from fastapi.testclient import TestClient

from main import app, count_tickets_by_story, Ticket

# Initialize TestClient for the FastAPI app
client = TestClient(app)


class TestCountTicketsByStory(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_tickets_by_story([]), {})

    def test_single(self):
        tickets = [Ticket(id="1", story_id="STORY-1")]
        self.assertEqual(count_tickets_by_story(tickets), {"STORY-1": 1})

    def test_multiple(self):
        tickets = [
            Ticket(id="1", story_id="STORY-1"),
            Ticket(id="2", story_id="STORY-1"),
            Ticket(id="3", story_id="STORY-2"),
        ]
        self.assertEqual(
            count_tickets_by_story(tickets), {"STORY-1": 2, "STORY-2": 1}
        )


class TestAPI(unittest.TestCase):
    def test_api_empty(self):
        response = client.post("/tickets/count", json=[])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})

    def test_api_data(self):
        payload = [
            {"id": "1", "story_id": "S1"},
            {"id": "2", "story_id": "S2"},
            {"id": "3", "story_id": "S1"},
        ]
        response = client.post("/tickets/count", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"S1": 2, "S2": 1})


if __name__ == "__main__":
    unittest.main()
