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


class V1beta1ACMECertificateDetails(object):
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
        'account_ref': 'str',
        'cert_stable_url': 'str',
        'cert_url': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'account_ref': 'accountRef',
        'cert_stable_url': 'certStableUrl',
        'cert_url': 'certUrl',
        'domain': 'domain'
    }

    def __init__(self, account_ref=None, cert_stable_url=None, cert_url=None, domain=None):
        """
        V1beta1ACMECertificateDetails - a model defined in Swagger
        """

        self._account_ref = None
        self._cert_stable_url = None
        self._cert_url = None
        self._domain = None
        self.discriminator = None

        if account_ref is not None:
          self.account_ref = account_ref
        self.cert_stable_url = cert_stable_url
        self.cert_url = cert_url
        self.domain = domain

    @property
    def account_ref(self):
        """
        Gets the account_ref of this V1beta1ACMECertificateDetails.

        :return: The account_ref of this V1beta1ACMECertificateDetails.
        :rtype: str
        """
        return self._account_ref

    @account_ref.setter
    def account_ref(self, account_ref):
        """
        Sets the account_ref of this V1beta1ACMECertificateDetails.

        :param account_ref: The account_ref of this V1beta1ACMECertificateDetails.
        :type: str
        """

        self._account_ref = account_ref

    @property
    def cert_stable_url(self):
        """
        Gets the cert_stable_url of this V1beta1ACMECertificateDetails.

        :return: The cert_stable_url of this V1beta1ACMECertificateDetails.
        :rtype: str
        """
        return self._cert_stable_url

    @cert_stable_url.setter
    def cert_stable_url(self, cert_stable_url):
        """
        Sets the cert_stable_url of this V1beta1ACMECertificateDetails.

        :param cert_stable_url: The cert_stable_url of this V1beta1ACMECertificateDetails.
        :type: str
        """
        if cert_stable_url is None:
            raise ValueError("Invalid value for `cert_stable_url`, must not be `None`")

        self._cert_stable_url = cert_stable_url

    @property
    def cert_url(self):
        """
        Gets the cert_url of this V1beta1ACMECertificateDetails.

        :return: The cert_url of this V1beta1ACMECertificateDetails.
        :rtype: str
        """
        return self._cert_url

    @cert_url.setter
    def cert_url(self, cert_url):
        """
        Sets the cert_url of this V1beta1ACMECertificateDetails.

        :param cert_url: The cert_url of this V1beta1ACMECertificateDetails.
        :type: str
        """
        if cert_url is None:
            raise ValueError("Invalid value for `cert_url`, must not be `None`")

        self._cert_url = cert_url

    @property
    def domain(self):
        """
        Gets the domain of this V1beta1ACMECertificateDetails.

        :return: The domain of this V1beta1ACMECertificateDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this V1beta1ACMECertificateDetails.

        :param domain: The domain of this V1beta1ACMECertificateDetails.
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")

        self._domain = domain

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
        if not isinstance(other, V1beta1ACMECertificateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
