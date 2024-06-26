# coding: utf-8

"""
    Telstra Messaging API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.2.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Telstra_Messaging_Old.configuration import Configuration


class GetSubscriptionResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'active_days': 'str',
        'notify_url': 'str',
        'destination_address': 'str'
    }

    attribute_map = {
        'active_days': 'activeDays',
        'notify_url': 'notifyURL',
        'destination_address': 'destinationAddress'
    }

    def __init__(self, active_days=None, notify_url=None, destination_address=None, local_vars_configuration=None):  # noqa: E501
        """GetSubscriptionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_days = None
        self._notify_url = None
        self._destination_address = None
        self.discriminator = None

        if active_days is not None:
            self.active_days = active_days
        if notify_url is not None:
            self.notify_url = notify_url
        if destination_address is not None:
            self.destination_address = destination_address

    @property
    def active_days(self):
        """Gets the active_days of this GetSubscriptionResponse.  # noqa: E501

        Number of active days  # noqa: E501

        :return: The active_days of this GetSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._active_days

    @active_days.setter
    def active_days(self, active_days):
        """Sets the active_days of this GetSubscriptionResponse.

        Number of active days  # noqa: E501

        :param active_days: The active_days of this GetSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._active_days = active_days

    @property
    def notify_url(self):
        """Gets the notify_url of this GetSubscriptionResponse.  # noqa: E501

        Notify url configured  # noqa: E501

        :return: The notify_url of this GetSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this GetSubscriptionResponse.

        Notify url configured  # noqa: E501

        :param notify_url: The notify_url of this GetSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

    @property
    def destination_address(self):
        """Gets the destination_address of this GetSubscriptionResponse.  # noqa: E501

        The mobile phone number that was allocated  # noqa: E501

        :return: The destination_address of this GetSubscriptionResponse.  # noqa: E501
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """Sets the destination_address of this GetSubscriptionResponse.

        The mobile phone number that was allocated  # noqa: E501

        :param destination_address: The destination_address of this GetSubscriptionResponse.  # noqa: E501
        :type: str
        """

        self._destination_address = destination_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetSubscriptionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSubscriptionResponse):
            return True

        return self.to_dict() != other.to_dict()
