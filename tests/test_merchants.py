from . import SdkBaseCase


class MerchantsTestCase(SdkBaseCase):

    def test_list(self):
        self.assertStatus(self.client.merchants(), 200)
