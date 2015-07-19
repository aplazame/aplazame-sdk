from .base import SdkBaseCase


class CustomersTestCase(SdkBaseCase):

    def test_list(self):
        response = self.client.customers()
        self.assertEqual(response.status_code, 200)
