# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Trip(object):
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
        'links': 'VehicleLinks',
        'included': 'list[ERRORUNKNOWN]',
        'data': 'TripResource'
    }

    attribute_map = {
        'links': 'links',
        'included': 'included',
        'data': 'data'
    }

    def __init__(self, links=None, included=None, data=None):
        """
        Trip - a model defined in Swagger
        """

        self._links = None
        self._included = None
        self._data = None

        if links is not None:
          self.links = links
        if included is not None:
          self.included = included
        self.data = data

    @property
    def links(self):
        """
        Gets the links of this Trip.

        :return: The links of this Trip.
        :rtype: VehicleLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Trip.

        :param links: The links of this Trip.
        :type: VehicleLinks
        """

        self._links = links

    @property
    def included(self):
        """
        Gets the included of this Trip.
        Included resources

        :return: The included of this Trip.
        :rtype: list[ERRORUNKNOWN]
        """
        return self._included

    @included.setter
    def included(self, included):
        """
        Sets the included of this Trip.
        Included resources

        :param included: The included of this Trip.
        :type: list[ERRORUNKNOWN]
        """

        self._included = included

    @property
    def data(self):
        """
        Gets the data of this Trip.

        :return: The data of this Trip.
        :rtype: TripResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this Trip.

        :param data: The data of this Trip.
        :type: TripResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

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
        if not isinstance(other, Trip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
