from django test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    def test_item_name_is_reqd(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required')

    def test_done_field_is_not_reqd(self)
        form = ItemForm({'name': 'Test'})
        self.assertTrue(form.is_valid())
