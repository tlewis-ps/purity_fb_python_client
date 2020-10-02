# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.1 Python SDK

    Pure Storage FlashBlade REST 1.1 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.1
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SnapshotSuffix(object):
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
        'suffix': 'str'
    }

    attribute_map = {
        'suffix': 'suffix'
    }

    def __init__(self, suffix=None):  # noqa: E501
        """SnapshotSuffix - a model defined in Swagger"""  # noqa: E501

        self._suffix = None
        self.discriminator = None

        self.suffix = suffix

    @property
    def suffix(self):
        """Gets the suffix of this SnapshotSuffix.  # noqa: E501

        the suffix of a snapshot  # noqa: E501

        :return: The suffix of this SnapshotSuffix.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this SnapshotSuffix.

        the suffix of a snapshot  # noqa: E501

        :param suffix: The suffix of this SnapshotSuffix.  # noqa: E501
        :type: str
        """
        if suffix is None:
            raise ValueError("Invalid value for `suffix`, must not be `None`")  # noqa: E501

        self._suffix = suffix

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
        if issubclass(SnapshotSuffix, dict):
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
        if not isinstance(other, SnapshotSuffix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
