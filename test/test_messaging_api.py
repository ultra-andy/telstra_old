# coding: utf-8

"""
    Telstra Messaging API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2.10
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import Telstra_Messaging_Old
from Telstra_Messaging_Old.api.messaging_api import MessagingApi  # noqa: E501
from Telstra_Messaging_Old.rest import ApiException


class TestMessagingApi(unittest.TestCase):
    """MessagingApi unit test stubs"""

    def setUp(self):
        self.api = Telstra_Messaging_Old.api.messaging_api.MessagingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_mms_status(self):
        """Test case for get_mms_status

        Get MMS Status  # noqa: E501
        """
        pass

    def test_get_sms_status(self):
        """Test case for get_sms_status

        Get SMS Status  # noqa: E501
        """
        pass

    def test_mms_health_check(self):
        """Test case for mms_health_check

        MMS Health Check  # noqa: E501
        """
        pass

    def test_retrieve_mms_replies(self):
        """Test case for retrieve_mms_replies

        Retrieve MMS Replies  # noqa: E501
        """
        pass

    def test_retrieve_sms_replies(self):
        """Test case for retrieve_sms_replies

        Retrieve SMS Replies  # noqa: E501
        """
        pass

    def test_send_mms(self):
        """Test case for send_mms

        Send MMS  # noqa: E501
        """
        pass

    def test_send_multiple_sms(self):
        """Test case for send_multiple_sms

        Send Multiple SMS  # noqa: E501
        """
        pass

    def test_send_sms(self):
        """Test case for send_sms

        Send SMS  # noqa: E501
        """
        pass

    def test_sms_health_check(self):
        """Test case for sms_health_check

        SMS Health Check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
