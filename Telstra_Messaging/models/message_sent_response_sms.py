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

from Telstra_Messaging.configuration import Configuration


class MessageSentResponseSms(object):
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
        'messages': 'list[Message]',
        'country': 'list[object]',
        'message_type': 'str',
        'number_segments': 'int'
    }

    attribute_map = {
        'messages': 'messages',
        'country': 'Country',
        'message_type': 'messageType',
        'number_segments': 'numberSegments'
    }

    def __init__(self, messages=None, country=None, message_type=None, number_segments=None, local_vars_configuration=None):  # noqa: E501
        """MessageSentResponseSms - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._messages = None
        self._country = None
        self._message_type = None
        self._number_segments = None
        self.discriminator = None

        self.messages = messages
        if country is not None:
            self.country = country
        self.message_type = message_type
        self.number_segments = number_segments

    @property
    def messages(self):
        """Gets the messages of this MessageSentResponseSms.  # noqa: E501

        An array of messages.  # noqa: E501

        :return: The messages of this MessageSentResponseSms.  # noqa: E501
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this MessageSentResponseSms.

        An array of messages.  # noqa: E501

        :param messages: The messages of this MessageSentResponseSms.  # noqa: E501
        :type: list[Message]
        """
        if self.local_vars_configuration.client_side_validation and messages is None:  # noqa: E501
            raise ValueError("Invalid value for `messages`, must not be `None`")  # noqa: E501

        self._messages = messages

    @property
    def country(self):
        """Gets the country of this MessageSentResponseSms.  # noqa: E501

        An array of the countries to which the destination MSISDNs belong.  # noqa: E501

        :return: The country of this MessageSentResponseSms.  # noqa: E501
        :rtype: list[object]
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this MessageSentResponseSms.

        An array of the countries to which the destination MSISDNs belong.  # noqa: E501

        :param country: The country of this MessageSentResponseSms.  # noqa: E501
        :type: list[object]
        """

        self._country = country

    @property
    def message_type(self):
        """Gets the message_type of this MessageSentResponseSms.  # noqa: E501

        This returns whether the message sent was a SMS or MMS.  # noqa: E501

        :return: The message_type of this MessageSentResponseSms.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this MessageSentResponseSms.

        This returns whether the message sent was a SMS or MMS.  # noqa: E501

        :param message_type: The message_type of this MessageSentResponseSms.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message_type is None:  # noqa: E501
            raise ValueError("Invalid value for `message_type`, must not be `None`")  # noqa: E501

        self._message_type = message_type

    @property
    def number_segments(self):
        """Gets the number_segments of this MessageSentResponseSms.  # noqa: E501

        A message which has 160 GSM-7 characters or less will have numberSegments=1. Note that multi-part messages which are over 160 GSM-7 characters will include the User Data Header as part of the numberSegments. The User Data Header is being used for the re-assembly of the messages.   # noqa: E501

        :return: The number_segments of this MessageSentResponseSms.  # noqa: E501
        :rtype: int
        """
        return self._number_segments

    @number_segments.setter
    def number_segments(self, number_segments):
        """Sets the number_segments of this MessageSentResponseSms.

        A message which has 160 GSM-7 characters or less will have numberSegments=1. Note that multi-part messages which are over 160 GSM-7 characters will include the User Data Header as part of the numberSegments. The User Data Header is being used for the re-assembly of the messages.   # noqa: E501

        :param number_segments: The number_segments of this MessageSentResponseSms.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_segments is None:  # noqa: E501
            raise ValueError("Invalid value for `number_segments`, must not be `None`")  # noqa: E501

        self._number_segments = number_segments

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
        if not isinstance(other, MessageSentResponseSms):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageSentResponseSms):
            return True

        return self.to_dict() != other.to_dict()
