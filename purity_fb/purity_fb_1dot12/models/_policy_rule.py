# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.12 Python SDK

    Pure Storage FlashBlade REST 1.12 Python SDK. Compatible with REST API versions 1.0 - 1.12. Developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.12
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PolicyRule(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

#BEGIN_CUSTOM
    # IR-51527: Prevent Pytest from attempting to collect this class based on name.
    __test__ = False
#END_CUSTOM

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'keep_for': 'int',
        'every': 'int',
        'at': 'int',
        'time_zone': 'str'
    }

    attribute_map = {
        'keep_for': 'keep_for',
        'every': 'every',
        'at': 'at',
        'time_zone': 'time_zone'
    }

    def __init__(self, keep_for=None, every=None, at=None, time_zone=None):  # noqa: E501
        """PolicyRule - a model defined in Swagger"""  # noqa: E501

        self._keep_for = None
        self._every = None
        self._at = None
        self._time_zone = None
        self.discriminator = None

        if keep_for is not None:
            self.keep_for = keep_for
        if every is not None:
            self.every = every
        if at is not None:
            self.at = at
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def keep_for(self):
        """Gets the keep_for of this PolicyRule.  # noqa: E501

        how long we keep the snapshots  # noqa: E501

        :return: The keep_for of this PolicyRule.  # noqa: E501
        :rtype: int
        """
        return self._keep_for

    @keep_for.setter
    def keep_for(self, keep_for):
        """Sets the keep_for of this PolicyRule.

        how long we keep the snapshots  # noqa: E501

        :param keep_for: The keep_for of this PolicyRule.  # noqa: E501
        :type: int
        """

        self._keep_for = keep_for

    @property
    def every(self):
        """Gets the every of this PolicyRule.  # noqa: E501

        interval between we create a snapshot  # noqa: E501

        :return: The every of this PolicyRule.  # noqa: E501
        :rtype: int
        """
        return self._every

    @every.setter
    def every(self, every):
        """Sets the every of this PolicyRule.

        interval between we create a snapshot  # noqa: E501

        :param every: The every of this PolicyRule.  # noqa: E501
        :type: int
        """

        self._every = every

    @property
    def at(self):
        """Gets the at of this PolicyRule.  # noqa: E501

        time during the day, only valid if frequency is in days  # noqa: E501

        :return: The at of this PolicyRule.  # noqa: E501
        :rtype: int
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this PolicyRule.

        time during the day, only valid if frequency is in days  # noqa: E501

        :param at: The at of this PolicyRule.  # noqa: E501
        :type: int
        """

        self._at = at

    @property
    def time_zone(self):
        """Gets the time_zone of this PolicyRule.  # noqa: E501

        time zone used for at field.  # noqa: E501

        :return: The time_zone of this PolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this PolicyRule.

        time zone used for at field.  # noqa: E501

        :param time_zone: The time_zone of this PolicyRule.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PolicyRule, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
