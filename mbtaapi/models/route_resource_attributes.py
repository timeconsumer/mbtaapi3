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


class RouteResourceAttributes(object):
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
        'type': 'int',
        'sort_order': 'int',
        'short_name': 'str',
        'long_name': 'str',
        'direction_names': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'type': 'type',
        'sort_order': 'sort_order',
        'short_name': 'short_name',
        'long_name': 'long_name',
        'direction_names': 'direction_names',
        'description': 'description'
    }

    def __init__(self, type=None, sort_order=None, short_name=None, long_name=None, direction_names=None, description=None):
        """
        RouteResourceAttributes - a model defined in Swagger
        """

        self._type = None
        self._sort_order = None
        self._short_name = None
        self._long_name = None
        self._direction_names = None
        self._description = None

        if type is not None:
          self.type = type
        if sort_order is not None:
          self.sort_order = sort_order
        if short_name is not None:
          self.short_name = short_name
        if long_name is not None:
          self.long_name = long_name
        if direction_names is not None:
          self.direction_names = direction_names
        if description is not None:
          self.description = description

    @property
    def type(self):
        """
        Gets the type of this RouteResourceAttributes.
        | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            | 

        :return: The type of this RouteResourceAttributes.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RouteResourceAttributes.
        | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            | 

        :param type: The type of this RouteResourceAttributes.
        :type: int
        """

        self._type = type

    @property
    def sort_order(self):
        """
        Gets the sort_order of this RouteResourceAttributes.
        Routes sort in ascending order

        :return: The sort_order of this RouteResourceAttributes.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this RouteResourceAttributes.
        Routes sort in ascending order

        :param sort_order: The sort_order of this RouteResourceAttributes.
        :type: int
        """

        self._sort_order = sort_order

    @property
    def short_name(self):
        """
        Gets the short_name of this RouteResourceAttributes.
        This will often be a short, abstract identifier like \"32\", \"100X\", or \"Green\" that riders use to identify a route, but which doesn't give any indication of what places the route serves. See [GTFS `routes.txt` `route_short_name`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt). 

        :return: The short_name of this RouteResourceAttributes.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this RouteResourceAttributes.
        This will often be a short, abstract identifier like \"32\", \"100X\", or \"Green\" that riders use to identify a route, but which doesn't give any indication of what places the route serves. See [GTFS `routes.txt` `route_short_name`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt). 

        :param short_name: The short_name of this RouteResourceAttributes.
        :type: str
        """

        self._short_name = short_name

    @property
    def long_name(self):
        """
        Gets the long_name of this RouteResourceAttributes.
        The full name of a route. This name is generally more descriptive than the `short_name` and will often include the route's destination or stop. See [GTFS `routes.txt` `route_long_name`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt). 

        :return: The long_name of this RouteResourceAttributes.
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """
        Sets the long_name of this RouteResourceAttributes.
        The full name of a route. This name is generally more descriptive than the `short_name` and will often include the route's destination or stop. See [GTFS `routes.txt` `route_long_name`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt). 

        :param long_name: The long_name of this RouteResourceAttributes.
        :type: str
        """

        self._long_name = long_name

    @property
    def direction_names(self):
        """
        Gets the direction_names of this RouteResourceAttributes.

        :return: The direction_names of this RouteResourceAttributes.
        :rtype: list[str]
        """
        return self._direction_names

    @direction_names.setter
    def direction_names(self, direction_names):
        """
        Sets the direction_names of this RouteResourceAttributes.

        :param direction_names: The direction_names of this RouteResourceAttributes.
        :type: list[str]
        """

        self._direction_names = direction_names

    @property
    def description(self):
        """
        Gets the description of this RouteResourceAttributes.
        Details about stops, schedule, and/or service.  See [GTFS `routes.txt` `route_desc`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt). 

        :return: The description of this RouteResourceAttributes.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RouteResourceAttributes.
        Details about stops, schedule, and/or service.  See [GTFS `routes.txt` `route_desc`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt). 

        :param description: The description of this RouteResourceAttributes.
        :type: str
        """

        self._description = description

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
        if not isinstance(other, RouteResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
