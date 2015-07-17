from . import SdkBaseCase


class CustomersTestCase(SdkBaseCase):

    def test_list(self):
        self.assertStatus(self.client.customers(), 200)
