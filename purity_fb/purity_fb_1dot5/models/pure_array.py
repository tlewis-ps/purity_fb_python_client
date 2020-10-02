# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.5 Python SDK

    Pure Storage FlashBlade REST 1.5 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.5
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PureArray(object):
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
        'ntp_servers': 'list[str]',
        'os': 'str',
        'revision': 'str',
        'time_zone': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'ntp_servers': 'ntp_servers',
        'os': 'os',
        'revision': 'revision',
        'time_zone': 'time_zone',
        'version': 'version'
    }

    def __init__(self, name=None, id=None, ntp_servers=None, os=None, revision=None, time_zone=None, version=None):  # noqa: E501
        """PureArray - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._ntp_servers = None
        self._os = None
        self._revision = None
        self._time_zone = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if os is not None:
            self.os = os
        if revision is not None:
            self.revision = revision
        if time_zone is not None:
            self.time_zone = time_zone
        if version is not None:
            self.version = version

    @property
    def name(self):
        """Gets the name of this PureArray.  # noqa: E501

        The name of the object  # noqa: E501

        :return: The name of this PureArray.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PureArray.

        The name of the object  # noqa: E501

        :param name: The name of this PureArray.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this PureArray.  # noqa: E501

        A globally unique ID chosen by the system. Cannot change. Cannot ever refer to another resource.  # noqa: E501

        :return: The id of this PureArray.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PureArray.

        A globally unique ID chosen by the system. Cannot change. Cannot ever refer to another resource.  # noqa: E501

        :param id: The id of this PureArray.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this PureArray.  # noqa: E501


        :return: The ntp_servers of this PureArray.  # noqa: E501
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this PureArray.


        :param ntp_servers: The ntp_servers of this PureArray.  # noqa: E501
        :type: list[str]
        """

        self._ntp_servers = ntp_servers

    @property
    def os(self):
        """Gets the os of this PureArray.  # noqa: E501

        Possible values are Purity//FA and Purity//FB.  # noqa: E501

        :return: The os of this PureArray.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this PureArray.

        Possible values are Purity//FA and Purity//FB.  # noqa: E501

        :param os: The os of this PureArray.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def revision(self):
        """Gets the revision of this PureArray.  # noqa: E501


        :return: The revision of this PureArray.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PureArray.


        :param revision: The revision of this PureArray.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def time_zone(self):
        """Gets the time_zone of this PureArray.  # noqa: E501


        :return: The time_zone of this PureArray.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this PureArray.


        :param time_zone: The time_zone of this PureArray.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def version(self):
        """Gets the version of this PureArray.  # noqa: E501


        :return: The version of this PureArray.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PureArray.


        :param version: The version of this PureArray.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(PureArray, dict):
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
        if not isinstance(other, PureArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
