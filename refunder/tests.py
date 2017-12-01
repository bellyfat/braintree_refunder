from django.test import TestCase
import os

from .forms import RefunderForm

class NewRefundPageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_refunder_from(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], RefunderForm)

class RefundPageTest(TestCase):

    def test_POST_to_refund_redirects_to_refunding_page(self):
        dummy_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'functional_tests', 'dummy_source.csv')
        with open(dummy_file) as fp:
            response = self.client.post('/refund', {'environment': 'sandbox', 'merchant_id': 'asdf', 'public_key': 'asdf', 'private_key': 'asdf', 'source_csv': fp})
        self.assertRedirects(response, '/refunding')
    

