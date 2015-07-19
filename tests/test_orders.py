from datetime import datetime
from .base import SdkBaseCase


class OrdersTestCase(SdkBaseCase):

    def setUp(self):
        super(OrdersTestCase, self).setUp()

        results = self.client.orders({
            'confirmed_until': datetime.now()
        }).json()['results']

        self.order = results[0] if results else None

    def _order_required(f):
        def wrapped(self, *args, **kwargs):
            if self.order is not None:
                return f(self, *args, **kwargs)
        return wrapped

    def test_list(self):
        response = self.client.orders()
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        response = self.client.orders(page=2)
        self.assertEqual(response.status_code, 200)

    @_order_required
    def test_detail(self):
        response = self.client.order_detail(self.order['id'])
        self.assertEqual(response.status_code, 200)

    @_order_required
    def test_refund_check(self):
        response = self.client.refund_check(self.order['mid'])
        self.assertEqual(response.status_code, 200)

    @_order_required
    def test_refund(self):
        response = self.client.refund(self.order['mid'], amount=1)
        self.assertEqual(response.status_code, 200)

    @_order_required
    def test_authorize(self):
        response = self.client.authorize(self.order['mid'])
        self.assertEqual(response.status_code, 200)
