from django.test import TestCase
import datetime

class TasksTestCase(TestCase):

    def test_task_1(self):
        """Should return Hello World while GETing to /hello-world URL"""
        response = self.client.get('/hello-world/')
        assert response.status_code == 200
        assert 'Hello World' in str(response.content)

    def test_date(self):
        """Should return today's date in response."""
        response = self.client.get('/current_date/')
        assert response.status_code == 200
        assert datetime.date.today().strftime("Today is %d, %V %Y") in str(response.content)
