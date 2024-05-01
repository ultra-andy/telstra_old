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


class SendMmsRequest(object):
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
        '_from': 'str',
        'subject': 'str',
        'notify_url': 'str',
        'reply_request': 'bool',
        'mms_content': 'list[MMSContent]'
    }

    attribute_map = {
        'to': 'to',
        '_from': 'from',
        'subject': 'subject',
        'notify_url': 'notifyURL',
        'reply_request': 'replyRequest',
        'mms_content': 'MMSContent'
    }

    def __init__(self, to=None, _from=None, subject=None, notify_url=None, reply_request=None, mms_content=None, local_vars_configuration=None):  # noqa: E501
        """SendMmsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self.__from = None
        self._subject = None
        self._notify_url = None
        self._reply_request = None
        self._mms_content = None
        self.discriminator = None

        self.to = to
        if _from is not None:
            self._from = _from
        if subject is not None:
            self.subject = subject
        if notify_url is not None:
            self.notify_url = notify_url
        if reply_request is not None:
            self.reply_request = reply_request
        self.mms_content = mms_content

    @property
    def to(self):
        """Gets the to of this SendMmsRequest.  # noqa: E501

        This is the destination address. Can be an array of strings if sending to multiple numbers: \"to\":[\"+61412345678\", \"+61418765432\"]   # noqa: E501

        :return: The to of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendMmsRequest.

        This is the destination address. Can be an array of strings if sending to multiple numbers: \"to\":[\"+61412345678\", \"+61418765432\"]   # noqa: E501

        :param to: The to of this SendMmsRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this SendMmsRequest.  # noqa: E501

        This will be the source address that will be displayed on the receiving device. You can set an Alphanumeric sender ID of up to 11 characters that the MMS was sent from. Phone numbers in the `from` attribute will be blocked (400-error) to prevent number spoofing.  Most standard ASCII characters are accepted in the alphanumeric `from` attribute, however there are some limitations. The following limitations and characters are allowed in the alphanumeric `from` attribute; any alphabetic character (e.g. `abc`), any number mixed with alphabetic characters (e.g. `123abc`), uppercase and lowercase characters (e.g. `aBc`), any of the following special characters mixed with alphabetic characters are allowed; `~!@#$%^&*()~_~+-={}|[];'?,./` (e.g. `abc~!@`), any combination of lowercase, uppercase, numeric or allowed special characters (e.g. `abc@#123DE`). All other characters, including spaces and extended ASCII characters, are not allowed (e.g. `<>:\"\\`).  If attribute is not present, the service will use the mobile number associated with the application (in E.164 format).  If `replyRequest` is set to true, this field should not be present.  This feature is only available on Telstra Account paid plans, not through Free Trials or credit card paid plans.   *Please note:*  *- Alphanumeric sender ID works for domestic, i.e. Australian, destinations only.*  *- When Alphanumeric sender ID is used in sending MMS, Delivery Receipts will NOT be returned.*   # noqa: E501

        :return: The _from of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendMmsRequest.

        This will be the source address that will be displayed on the receiving device. You can set an Alphanumeric sender ID of up to 11 characters that the MMS was sent from. Phone numbers in the `from` attribute will be blocked (400-error) to prevent number spoofing.  Most standard ASCII characters are accepted in the alphanumeric `from` attribute, however there are some limitations. The following limitations and characters are allowed in the alphanumeric `from` attribute; any alphabetic character (e.g. `abc`), any number mixed with alphabetic characters (e.g. `123abc`), uppercase and lowercase characters (e.g. `aBc`), any of the following special characters mixed with alphabetic characters are allowed; `~!@#$%^&*()~_~+-={}|[];'?,./` (e.g. `abc~!@`), any combination of lowercase, uppercase, numeric or allowed special characters (e.g. `abc@#123DE`). All other characters, including spaces and extended ASCII characters, are not allowed (e.g. `<>:\"\\`).  If attribute is not present, the service will use the mobile number associated with the application (in E.164 format).  If `replyRequest` is set to true, this field should not be present.  This feature is only available on Telstra Account paid plans, not through Free Trials or credit card paid plans.   *Please note:*  *- Alphanumeric sender ID works for domestic, i.e. Australian, destinations only.*  *- When Alphanumeric sender ID is used in sending MMS, Delivery Receipts will NOT be returned.*   # noqa: E501

        :param _from: The _from of this SendMmsRequest.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def subject(self):
        """Gets the subject of this SendMmsRequest.  # noqa: E501

        The subject that will be used in an MMS message. Subject is limited to maximum of 64 characters.  Some special characters need to be encoded if used in the `subject` field (e.g. &amp;amp; for & and &amp;lt; for <).   # noqa: E501

        :return: The subject of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SendMmsRequest.

        The subject that will be used in an MMS message. Subject is limited to maximum of 64 characters.  Some special characters need to be encoded if used in the `subject` field (e.g. &amp;amp; for & and &amp;lt; for <).   # noqa: E501

        :param subject: The subject of this SendMmsRequest.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def notify_url(self):
        """Gets the notify_url of this SendMmsRequest.  # noqa: E501

        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc. Please refer to the Delivery Status section for more information.  If you are using a domain URL you must include the forward slash at the end of the URL (e.g. http://www.example.com/).   # noqa: E501

        :return: The notify_url of this SendMmsRequest.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this SendMmsRequest.

        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc. Please refer to the Delivery Status section for more information.  If you are using a domain URL you must include the forward slash at the end of the URL (e.g. http://www.example.com/).   # noqa: E501

        :param notify_url: The notify_url of this SendMmsRequest.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

    @property
    def reply_request(self):
        """Gets the reply_request of this SendMmsRequest.  # noqa: E501

        If set to true, the reply message functionality will be implemented. The `from` field should not be present.   # noqa: E501

        :return: The reply_request of this SendMmsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reply_request

    @reply_request.setter
    def reply_request(self, reply_request):
        """Sets the reply_request of this SendMmsRequest.

        If set to true, the reply message functionality will be implemented. The `from` field should not be present.   # noqa: E501

        :param reply_request: The reply_request of this SendMmsRequest.  # noqa: E501
        :type: bool
        """

        self._reply_request = reply_request

    @property
    def mms_content(self):
        """Gets the mms_content of this SendMmsRequest.  # noqa: E501

        An array of content that will be sent in an MMS message. If this array is present it will cause the `body` element to be ignored, and the message will be sent as an MMS.   # noqa: E501

        :return: The mms_content of this SendMmsRequest.  # noqa: E501
        :rtype: list[MMSContent]
        """
        return self._mms_content

    @mms_content.setter
    def mms_content(self, mms_content):
        """Sets the mms_content of this SendMmsRequest.

        An array of content that will be sent in an MMS message. If this array is present it will cause the `body` element to be ignored, and the message will be sent as an MMS.   # noqa: E501

        :param mms_content: The mms_content of this SendMmsRequest.  # noqa: E501
        :type: list[MMSContent]
        """
        if self.local_vars_configuration.client_side_validation and mms_content is None:  # noqa: E501
            raise ValueError("Invalid value for `mms_content`, must not be `None`")  # noqa: E501

        self._mms_content = mms_content

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
        if not isinstance(other, SendMmsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendMmsRequest):
            return True

        return self.to_dict() != other.to_dict()