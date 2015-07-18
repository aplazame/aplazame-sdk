from .base import SdkBaseCase


class OrdersTestCase(SdkBaseCase):

    def test_list(self):
        self.assertStatus(self.client.orders(), 200)
