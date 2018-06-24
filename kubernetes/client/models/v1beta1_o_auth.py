# coding: utf-8

"""
    Voyager

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v7.1.1
    Contact: hello@appscode.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1OAuth(object):
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
        'auth_backend': 'str',
        'auth_path': 'str',
        'host': 'str',
        'paths': 'list[str]',
        'signin_path': 'str'
    }

    attribute_map = {
        'auth_backend': 'authBackend',
        'auth_path': 'authPath',
        'host': 'host',
        'paths': 'paths',
        'signin_path': 'signinPath'
    }

    def __init__(self, auth_backend=None, auth_path=None, host=None, paths=None, signin_path=None):
        """
        V1beta1OAuth - a model defined in Swagger
        """

        self._auth_backend = None
        self._auth_path = None
        self._host = None
        self._paths = None
        self._signin_path = None
        self.discriminator = None

        if auth_backend is not None:
          self.auth_backend = auth_backend
        if auth_path is not None:
          self.auth_path = auth_path
        if host is not None:
          self.host = host
        if paths is not None:
          self.paths = paths
        if signin_path is not None:
          self.signin_path = signin_path

    @property
    def auth_backend(self):
        """
        Gets the auth_backend of this V1beta1OAuth.

        :return: The auth_backend of this V1beta1OAuth.
        :rtype: str
        """
        return self._auth_backend

    @auth_backend.setter
    def auth_backend(self, auth_backend):
        """
        Sets the auth_backend of this V1beta1OAuth.

        :param auth_backend: The auth_backend of this V1beta1OAuth.
        :type: str
        """

        self._auth_backend = auth_backend

    @property
    def auth_path(self):
        """
        Gets the auth_path of this V1beta1OAuth.

        :return: The auth_path of this V1beta1OAuth.
        :rtype: str
        """
        return self._auth_path

    @auth_path.setter
    def auth_path(self, auth_path):
        """
        Sets the auth_path of this V1beta1OAuth.

        :param auth_path: The auth_path of this V1beta1OAuth.
        :type: str
        """

        self._auth_path = auth_path

    @property
    def host(self):
        """
        Gets the host of this V1beta1OAuth.

        :return: The host of this V1beta1OAuth.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this V1beta1OAuth.

        :param host: The host of this V1beta1OAuth.
        :type: str
        """

        self._host = host

    @property
    def paths(self):
        """
        Gets the paths of this V1beta1OAuth.

        :return: The paths of this V1beta1OAuth.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this V1beta1OAuth.

        :param paths: The paths of this V1beta1OAuth.
        :type: list[str]
        """

        self._paths = paths

    @property
    def signin_path(self):
        """
        Gets the signin_path of this V1beta1OAuth.

        :return: The signin_path of this V1beta1OAuth.
        :rtype: str
        """
        return self._signin_path

    @signin_path.setter
    def signin_path(self, signin_path):
        """
        Sets the signin_path of this V1beta1OAuth.

        :param signin_path: The signin_path of this V1beta1OAuth.
        :type: str
        """

        self._signin_path = signin_path

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
        if not isinstance(other, V1beta1OAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
