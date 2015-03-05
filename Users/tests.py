from django.test import TestCase
from .models import *


# Create your tests here.
class UserCreateTests(TestCase):

    def setUp(self):
        pass

    def test_createValidUser(self):
        user = Account.objects.create_user('kspacey', 'kevin', 'spacey',
                'kspacey@kspacey.com', password='blah')

        c = Account.objects.get(username='kspacey')
        self.assertEqual(c.username, 'kspacey')
        self.assertEqual(c.first_name, 'kevin')
        self.assertEqual(c.last_name, 'spacey')
        self.assertEqual(c.email, 'kspacey@kspacey.com')
        self.assertFalse(c.is_superuser)
        self.assertFalse(c.is_staff)
        self.assertTrue(c.is_active)

    def test_createSuperUser(self):
        user = Account.objects.create_superuser('kspacey2', 'kevin', 'spacey',
                'kspacey2@kspacey.com', password='blah')

        c = Account.objects.get(username='kspacey2')
        self.assertEqual(c.username, 'kspacey2')
        self.assertEqual(c.first_name, 'kevin')
        self.assertEqual(c.last_name, 'spacey')
        self.assertEqual(c.email, 'kspacey2@kspacey.com')
        self.assertTrue(c.is_superuser)
        self.assertTrue(c.is_staff)
        self.assertTrue(c.is_active)

    def test_get_full_name(self):
        user = Account.objects.create_user('jsmith', 'john', 'smith',
                'johnsmith@smith.com', password='blah')

        self.assertEqual(user.get_full_name(), "john smith")

    def test_get_short_name(self):
        user = Account.objects.create_user('msmith', 'mary', 'smith',
                'marysmith@smith.com', password='blah')

        self.assertEqual(user.get_short_name(), "mary")

    def test_unicode(self):
        user = Account.objects.create_user('jblack', 'jack', 'black',
                'jblack@blah.com', password='blah')

        self.assertEqual(user.__unicode__(), "jblack")
