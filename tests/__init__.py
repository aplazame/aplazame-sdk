import pytest
import unittest
import aplazame_sdk


@pytest.mark.usefixtures('conf_class')
class SdkBaseCase(unittest.TestCase):

    def setUp(self):
        # pytest.set_trace()
        if self.token is None:
            raise Exception('Todo: mocks')

        self.client = aplazame_sdk.Client(
            access_token=self.token, host=self.host, sandbox=True,
            version=self.version, verify=self.verify)

    def tearDown(self):
        pass

    def assertStatus(self, response, code):
        self.assertEqual(response.status_code, code)
