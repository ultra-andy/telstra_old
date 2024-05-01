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


class ProvisionNumberResponse(object):
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
        'destination_address': 'str',
        'expiry_date': 'float'
    }

    attribute_map = {
        'destination_address': 'destinationAddress',
        'expiry_date': 'expiryDate'
    }

    def __init__(self, destination_address=None, expiry_date=None, local_vars_configuration=None):  # noqa: E501
        """ProvisionNumberResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._destination_address = None
        self._expiry_date = None
        self.discriminator = None

        if destination_address is not None:
            self.destination_address = destination_address
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def destination_address(self):
        """Gets the destination_address of this ProvisionNumberResponse.  # noqa: E501

        The mobile phone number that was allocated  # noqa: E501

        :return: The destination_address of this ProvisionNumberResponse.  # noqa: E501
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """Sets the destination_address of this ProvisionNumberResponse.

        The mobile phone number that was allocated  # noqa: E501

        :param destination_address: The destination_address of this ProvisionNumberResponse.  # noqa: E501
        :type: str
        """

        self._destination_address = destination_address

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ProvisionNumberResponse.  # noqa: E501

        Free Trial apps can only add activeDays for their provisioned number every 30 days. This is in Unix time format.  # noqa: E501

        :return: The expiry_date of this ProvisionNumberResponse.  # noqa: E501
        :rtype: float
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ProvisionNumberResponse.

        Free Trial apps can only add activeDays for their provisioned number every 30 days. This is in Unix time format.  # noqa: E501

        :param expiry_date: The expiry_date of this ProvisionNumberResponse.  # noqa: E501
        :type: float
        """

        self._expiry_date = expiry_date

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
        if not isinstance(other, ProvisionNumberResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProvisionNumberResponse):
            return True

        return self.to_dict() != other.to_dict()