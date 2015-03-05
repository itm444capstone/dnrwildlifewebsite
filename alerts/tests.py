import datetime

from django.test import TestCase
from .models import *

# Create your tests here.
class TestAlert(TestCase):

    def setUp(self):
        pass

    def test_Alert_create(self):
        alert = Alert.objects.create(title="Aliens", text="Aliens have been sighted",
                published=True)
        t = datetime.datetime.now()

        c = Alert.objects.get(pk=1)

        self.assertEqual(c.title, "Aliens")
        self.assertEqual(c.text, "Aliens have been sighted")
        self.assertEqual(c.publish_date.minute, t.minute)
        self.assertEqual(c.publish_date.hour, t.hour)
        self.assertFalse(c.recurring)
        self.assertTrue(c.published)
