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


class Audit(object):
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
        'arguments': 'str',
        'command': 'str',
        'ip_address': 'str',
        'subcommand': 'str',
        'time': 'int',
        'user': 'str',
        'user_agent': 'str',
        'user_interface': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'arguments': 'arguments',
        'command': 'command',
        'ip_address': 'ip_address',
        'subcommand': 'subcommand',
        'time': 'time',
        'user': 'user',
        'user_agent': 'user_agent',
        'user_interface': 'user_interface'
    }

    def __init__(self, id=None, name=None, arguments=None, command=None, ip_address=None, subcommand=None, time=None, user=None, user_agent=None, user_interface=None):
        """
        Audit - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._arguments = None
        self._command = None
        self._ip_address = None
        self._subcommand = None
        self._time = None
        self._user = None
        self._user_agent = None
        self._user_interface = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if arguments is not None:
          self.arguments = arguments
        if command is not None:
          self.command = command
        if ip_address is not None:
          self.ip_address = ip_address
        if subcommand is not None:
          self.subcommand = subcommand
        if time is not None:
          self.time = time
        if user is not None:
          self.user = user
        if user_agent is not None:
          self.user_agent = user_agent
        if user_interface is not None:
          self.user_interface = user_interface

    @property
    def id(self):
        """
        Gets the id of this Audit.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this Audit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Audit.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this Audit.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Audit.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this Audit.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Audit.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this Audit.
        :type: str
        """

        self._name = name

    @property
    def arguments(self):
        """
        Gets the arguments of this Audit.

        :return: The arguments of this Audit.
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this Audit.

        :param arguments: The arguments of this Audit.
        :type: str
        """

        self._arguments = arguments

    @property
    def command(self):
        """
        Gets the command of this Audit.

        :return: The command of this Audit.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this Audit.

        :param command: The command of this Audit.
        :type: str
        """

        self._command = command

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Audit.

        :return: The ip_address of this Audit.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Audit.

        :param ip_address: The ip_address of this Audit.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def subcommand(self):
        """
        Gets the subcommand of this Audit.

        :return: The subcommand of this Audit.
        :rtype: str
        """
        return self._subcommand

    @subcommand.setter
    def subcommand(self, subcommand):
        """
        Sets the subcommand of this Audit.

        :param subcommand: The subcommand of this Audit.
        :type: str
        """

        self._subcommand = subcommand

    @property
    def time(self):
        """
        Gets the time of this Audit.

        :return: The time of this Audit.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this Audit.

        :param time: The time of this Audit.
        :type: int
        """

        self._time = time

    @property
    def user(self):
        """
        Gets the user of this Audit.

        :return: The user of this Audit.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Audit.

        :param user: The user of this Audit.
        :type: str
        """

        self._user = user

    @property
    def user_agent(self):
        """
        Gets the user_agent of this Audit.

        :return: The user_agent of this Audit.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this Audit.

        :param user_agent: The user_agent of this Audit.
        :type: str
        """

        self._user_agent = user_agent

    @property
    def user_interface(self):
        """
        Gets the user_interface of this Audit.
        The user interface through which the user session event was performed. Valid values are `CLI`, `GUI`, and `REST`.

        :return: The user_interface of this Audit.
        :rtype: str
        """
        return self._user_interface

    @user_interface.setter
    def user_interface(self, user_interface):
        """
        Sets the user_interface of this Audit.
        The user interface through which the user session event was performed. Valid values are `CLI`, `GUI`, and `REST`.

        :param user_interface: The user_interface of this Audit.
        :type: str
        """

        self._user_interface = user_interface

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
        if not isinstance(other, Audit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
