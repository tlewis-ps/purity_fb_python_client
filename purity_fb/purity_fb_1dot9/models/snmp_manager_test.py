# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.9 Python SDK

    Pure Storage FlashBlade REST 1.9 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.9
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SnmpManagerTest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'sent': 'bool',
        'error': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'sent': 'sent',
        'error': 'error'
    }

    def __init__(self, id=None, name=None, sent=None, error=None):
        """
        SnmpManagerTest - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._sent = None
        self._error = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if sent is not None:
          self.sent = sent
        if error is not None:
          self.error = error

    @property
    def id(self):
        """
        Gets the id of this SnmpManagerTest.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this SnmpManagerTest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SnmpManagerTest.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this SnmpManagerTest.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SnmpManagerTest.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this SnmpManagerTest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SnmpManagerTest.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this SnmpManagerTest.
        :type: str
        """

        self._name = name

    @property
    def sent(self):
        """
        Gets the sent of this SnmpManagerTest.
        Is the test trap or inform sent?

        :return: The sent of this SnmpManagerTest.
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """
        Sets the sent of this SnmpManagerTest.
        Is the test trap or inform sent?

        :param sent: The sent of this SnmpManagerTest.
        :type: bool
        """

        self._sent = sent

    @property
    def error(self):
        """
        Gets the error of this SnmpManagerTest.
        Error message (if failed).

        :return: The error of this SnmpManagerTest.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this SnmpManagerTest.
        Error message (if failed).

        :param error: The error of this SnmpManagerTest.
        :type: str
        """

        self._error = error

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SnmpManagerTest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
