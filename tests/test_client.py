import pytest
import aplazame_sdk

from .base import SdkBaseCase


class ClientTestCase(SdkBaseCase):

    def test_delete(self):
        with pytest.raises(aplazame_sdk.AplazameError) as excinfo:
            self.client.delete('/orders')
        self.assertEqual(excinfo.value.code, 405)
