from django test import TestCase
from .models import Item

def test_get_base_template(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)