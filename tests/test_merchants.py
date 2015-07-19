from .base import SdkBaseCase


class MerchantsTestCase(SdkBaseCase):

    def test_list(self):
        response = self.client.merchants()
        self.assertEqual(response.status_code, 200)
