import pytest
import aplazame_sdk

from .base import SdkBaseCase


class CustomersTestCase(SdkBaseCase):

    def setUp(self):
        super(CustomersTestCase, self).setUp()

        results = self.client.customers().json()['results']
        self.customer = results[0] if results else None

    def _customer_required(f):
        def wrapped(self, *args, **kwargs):
            if self.customer is not None:
                return f(self, *args, **kwargs)
        return wrapped

    def test_list(self):
        response = self.client.customers()
        self.assertEqual(response.status_code, 200)

    @_customer_required
    def test_detail(self):
        response = self.client.customer_detail(self.customer['id'])
        self.assertEqual(response.status_code, 200)

    @_customer_required
    def _test_history(self):
        response = self.client.customer_history(self.customer['id'])
        self.assertEqual(response.status_code, 200)

    @_customer_required
    def test_defaults(self):
        with pytest.raises(aplazame_sdk.AplazameError) as excinfo:
            self.client.defaults(self.customer['id'])

        self.assertEqual(excinfo.value.code, 403)

    @_customer_required
    def test_default_history(self):
        with pytest.raises(aplazame_sdk.AplazameError) as excinfo:
            self.client.default_history(self.customer['id'], 0)

        self.assertEqual(excinfo.value.code, 404)
