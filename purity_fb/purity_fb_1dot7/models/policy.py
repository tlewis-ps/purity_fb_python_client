# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.7 Python SDK

    Pure Storage FlashBlade REST 1.7 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.7
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Policy(object):
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
        'name': 'str',
        'id': 'str',
        'enabled': 'bool',
        'rules': 'list[ResourceRule]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'enabled': 'enabled',
        'rules': 'rules'
    }

    def __init__(self, name=None, id=None, enabled=None, rules=None):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._enabled = None
        self._rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if rules is not None:
            self.rules = rules

    @property
    def name(self):
        """Gets the name of this Policy.  # noqa: E501

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :return: The name of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.

        The name of the object (e.g., a file system or snapshot)  # noqa: E501

        :param name: The name of this Policy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this Policy.  # noqa: E501

        A unique ID chosen by the system. Cannot change.  # noqa: E501

        :return: The id of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Policy.

        A unique ID chosen by the system. Cannot change.  # noqa: E501

        :param id: The id of this Policy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def enabled(self):
        """Gets the enabled of this Policy.  # noqa: E501

        Indicates if policy is enabled (true) or disabled (false). Enabled by default.  # noqa: E501

        :return: The enabled of this Policy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Policy.

        Indicates if policy is enabled (true) or disabled (false). Enabled by default.  # noqa: E501

        :param enabled: The enabled of this Policy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def rules(self):
        """Gets the rules of this Policy.  # noqa: E501


        :return: The rules of this Policy.  # noqa: E501
        :rtype: list[ResourceRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Policy.


        :param rules: The rules of this Policy.  # noqa: E501
        :type: list[ResourceRule]
        """

        self._rules = rules

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
        if issubclass(Policy, dict):
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
