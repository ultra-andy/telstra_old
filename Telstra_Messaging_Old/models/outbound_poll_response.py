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


class OutboundPollResponse(object):
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
        'to': 'str',
        'sent_timestamp': 'str',
        'received_timestamp': 'str',
        'delivery_status': 'Status'
    }

    attribute_map = {
        'to': 'to',
        'sent_timestamp': 'sentTimestamp',
        'received_timestamp': 'receivedTimestamp',
        'delivery_status': 'deliveryStatus'
    }

    def __init__(self, to=None, sent_timestamp=None, received_timestamp=None, delivery_status=None, local_vars_configuration=None):  # noqa: E501
        """OutboundPollResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self._sent_timestamp = None
        self._received_timestamp = None
        self._delivery_status = None
        self.discriminator = None

        if to is not None:
            self.to = to
        if sent_timestamp is not None:
            self.sent_timestamp = sent_timestamp
        if received_timestamp is not None:
            self.received_timestamp = received_timestamp
        if delivery_status is not None:
            self.delivery_status = delivery_status

    @property
    def to(self):
        """Gets the to of this OutboundPollResponse.  # noqa: E501

        The phone number (recipient) the message was sent to (in E.164 format).   # noqa: E501

        :return: The to of this OutboundPollResponse.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this OutboundPollResponse.

        The phone number (recipient) the message was sent to (in E.164 format).   # noqa: E501

        :param to: The to of this OutboundPollResponse.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def sent_timestamp(self):
        """Gets the sent_timestamp of this OutboundPollResponse.  # noqa: E501

        The date and time when the message was sent.  # noqa: E501

        :return: The sent_timestamp of this OutboundPollResponse.  # noqa: E501
        :rtype: str
        """
        return self._sent_timestamp

    @sent_timestamp.setter
    def sent_timestamp(self, sent_timestamp):
        """Sets the sent_timestamp of this OutboundPollResponse.

        The date and time when the message was sent.  # noqa: E501

        :param sent_timestamp: The sent_timestamp of this OutboundPollResponse.  # noqa: E501
        :type: str
        """

        self._sent_timestamp = sent_timestamp

    @property
    def received_timestamp(self):
        """Gets the received_timestamp of this OutboundPollResponse.  # noqa: E501

        The date and time when the message was recieved by recipient.  # noqa: E501

        :return: The received_timestamp of this OutboundPollResponse.  # noqa: E501
        :rtype: str
        """
        return self._received_timestamp

    @received_timestamp.setter
    def received_timestamp(self, received_timestamp):
        """Sets the received_timestamp of this OutboundPollResponse.

        The date and time when the message was recieved by recipient.  # noqa: E501

        :param received_timestamp: The received_timestamp of this OutboundPollResponse.  # noqa: E501
        :type: str
        """

        self._received_timestamp = received_timestamp

    @property
    def delivery_status(self):
        """Gets the delivery_status of this OutboundPollResponse.  # noqa: E501


        :return: The delivery_status of this OutboundPollResponse.  # noqa: E501
        :rtype: Status
        """
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, delivery_status):
        """Sets the delivery_status of this OutboundPollResponse.


        :param delivery_status: The delivery_status of this OutboundPollResponse.  # noqa: E501
        :type: Status
        """

        self._delivery_status = delivery_status

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
        if not isinstance(other, OutboundPollResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutboundPollResponse):
            return True

        return self.to_dict() != other.to_dict()
