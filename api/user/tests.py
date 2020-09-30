from django.test import TestCase


# Create your tests here.
class Demo(TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('tearDown')

    def test_Login_view(self):
        print('test_demo')
