# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server.models.operational_state_pac import OperationalStatePac  # noqa: F401,E501
from tapi_server.models.resource_spec import ResourceSpec  # noqa: F401,E501
from tapi_server.models.termination_pac import TerminationPac  # noqa: F401,E501
from tapi_server import util


class ConnectionEndPoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, name: List[NameAndValue]=None, operational_state: str=None, lifecycle_state: str=None, termination_direction: str=None, termination_state: str=None, layer_protocol_name: str=None, connectivity_service_end_point: str=None, parent_node_edge_point: List[str]=None, client_node_edge_point: List[str]=None, connection_port_direction: str=None, connection_port_role: str=None):  # noqa: E501
        """ConnectionEndPoint - a model defined in Swagger

        :param uuid: The uuid of this ConnectionEndPoint.  # noqa: E501
        :type uuid: str
        :param name: The name of this ConnectionEndPoint.  # noqa: E501
        :type name: List[NameAndValue]
        :param operational_state: The operational_state of this ConnectionEndPoint.  # noqa: E501
        :type operational_state: str
        :param lifecycle_state: The lifecycle_state of this ConnectionEndPoint.  # noqa: E501
        :type lifecycle_state: str
        :param termination_direction: The termination_direction of this ConnectionEndPoint.  # noqa: E501
        :type termination_direction: str
        :param termination_state: The termination_state of this ConnectionEndPoint.  # noqa: E501
        :type termination_state: str
        :param layer_protocol_name: The layer_protocol_name of this ConnectionEndPoint.  # noqa: E501
        :type layer_protocol_name: str
        :param connectivity_service_end_point: The connectivity_service_end_point of this ConnectionEndPoint.  # noqa: E501
        :type connectivity_service_end_point: str
        :param parent_node_edge_point: The parent_node_edge_point of this ConnectionEndPoint.  # noqa: E501
        :type parent_node_edge_point: List[str]
        :param client_node_edge_point: The client_node_edge_point of this ConnectionEndPoint.  # noqa: E501
        :type client_node_edge_point: List[str]
        :param connection_port_direction: The connection_port_direction of this ConnectionEndPoint.  # noqa: E501
        :type connection_port_direction: str
        :param connection_port_role: The connection_port_role of this ConnectionEndPoint.  # noqa: E501
        :type connection_port_role: str
        """
        self.swagger_types = {
            'uuid': str,
            'name': List[NameAndValue],
            'operational_state': str,
            'lifecycle_state': str,
            'termination_direction': str,
            'termination_state': str,
            'layer_protocol_name': str,
            'connectivity_service_end_point': str,
            'parent_node_edge_point': List[str],
            'client_node_edge_point': List[str],
            'connection_port_direction': str,
            'connection_port_role': str
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'name': 'name',
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'termination_direction': 'termination-direction',
            'termination_state': 'termination-state',
            'layer_protocol_name': 'layer-protocol-name',
            'connectivity_service_end_point': 'connectivity-service-end-point',
            'parent_node_edge_point': 'parent-node-edge-point',
            'client_node_edge_point': 'client-node-edge-point',
            'connection_port_direction': 'connection-port-direction',
            'connection_port_role': 'connection-port-role'
        }

        self._uuid = uuid
        self._name = name
        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._termination_direction = termination_direction
        self._termination_state = termination_state
        self._layer_protocol_name = layer_protocol_name
        self._connectivity_service_end_point = connectivity_service_end_point
        self._parent_node_edge_point = parent_node_edge_point
        self._client_node_edge_point = client_node_edge_point
        self._connection_port_direction = connection_port_direction
        self._connection_port_role = connection_port_role

    @classmethod
    def from_dict(cls, dikt) -> 'ConnectionEndPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The connection-end-point of this ConnectionEndPoint.  # noqa: E501
        :rtype: ConnectionEndPoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this ConnectionEndPoint.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this ConnectionEndPoint.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this ConnectionEndPoint.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this ConnectionEndPoint.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this ConnectionEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this ConnectionEndPoint.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this ConnectionEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this ConnectionEndPoint.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def operational_state(self) -> str:
        """Gets the operational_state of this ConnectionEndPoint.


        :return: The operational_state of this ConnectionEndPoint.
        :rtype: str
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state: str):
        """Sets the operational_state of this ConnectionEndPoint.


        :param operational_state: The operational_state of this ConnectionEndPoint.
        :type operational_state: str
        """
        allowed_values = ["DISABLED", "ENABLED"]  # noqa: E501
        if operational_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operational_state` ({0}), must be one of {1}"
                .format(operational_state, allowed_values)
            )

        self._operational_state = operational_state

    @property
    def lifecycle_state(self) -> str:
        """Gets the lifecycle_state of this ConnectionEndPoint.


        :return: The lifecycle_state of this ConnectionEndPoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state: str):
        """Sets the lifecycle_state of this ConnectionEndPoint.


        :param lifecycle_state: The lifecycle_state of this ConnectionEndPoint.
        :type lifecycle_state: str
        """
        allowed_values = ["PLANNED", "POTENTIAL_AVAILABLE", "POTENTIAL_BUSY", "INSTALLED", "PENDING_REMOVAL"]  # noqa: E501
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state` ({0}), must be one of {1}"
                .format(lifecycle_state, allowed_values)
            )

        self._lifecycle_state = lifecycle_state

    @property
    def termination_direction(self) -> str:
        """Gets the termination_direction of this ConnectionEndPoint.

        The overall directionality of the LP.  - A BIDIRECTIONAL LP will have some SINK and/or SOURCE flowss. - A SINK LP can only contain elements with SINK flows or CONTRA_DIRECTION_SOURCE flows - A SOURCE LP can only contain SOURCE flows or CONTRA_DIRECTION_SINK flows  # noqa: E501

        :return: The termination_direction of this ConnectionEndPoint.
        :rtype: str
        """
        return self._termination_direction

    @termination_direction.setter
    def termination_direction(self, termination_direction: str):
        """Sets the termination_direction of this ConnectionEndPoint.

        The overall directionality of the LP.  - A BIDIRECTIONAL LP will have some SINK and/or SOURCE flowss. - A SINK LP can only contain elements with SINK flows or CONTRA_DIRECTION_SOURCE flows - A SOURCE LP can only contain SOURCE flows or CONTRA_DIRECTION_SINK flows  # noqa: E501

        :param termination_direction: The termination_direction of this ConnectionEndPoint.
        :type termination_direction: str
        """
        allowed_values = ["BIDIRECTIONAL", "SINK", "SOURCE", "UNDEFINED_OR_UNKNOWN"]  # noqa: E501
        if termination_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `termination_direction` ({0}), must be one of {1}"
                .format(termination_direction, allowed_values)
            )

        self._termination_direction = termination_direction

    @property
    def termination_state(self) -> str:
        """Gets the termination_state of this ConnectionEndPoint.

        Indicates whether the layer is terminated and if so how.  # noqa: E501

        :return: The termination_state of this ConnectionEndPoint.
        :rtype: str
        """
        return self._termination_state

    @termination_state.setter
    def termination_state(self, termination_state: str):
        """Sets the termination_state of this ConnectionEndPoint.

        Indicates whether the layer is terminated and if so how.  # noqa: E501

        :param termination_state: The termination_state of this ConnectionEndPoint.
        :type termination_state: str
        """
        allowed_values = ["LP_CAN_NEVER_TERMINATE", "LT_NOT_TERMINATED", "TERMINATED_SERVER_TO_CLIENT_FLOW", "TERMINATED_CLIENT_TO_SERVER_FLOW", "TERMINATED_BIDIRECTIONAL", "LT_PERMENANTLY_TERMINATED", "TERMINATION_STATE_UNKNOWN"]  # noqa: E501
        if termination_state not in allowed_values:
            raise ValueError(
                "Invalid value for `termination_state` ({0}), must be one of {1}"
                .format(termination_state, allowed_values)
            )

        self._termination_state = termination_state

    @property
    def layer_protocol_name(self) -> str:
        """Gets the layer_protocol_name of this ConnectionEndPoint.


        :return: The layer_protocol_name of this ConnectionEndPoint.
        :rtype: str
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name: str):
        """Sets the layer_protocol_name of this ConnectionEndPoint.


        :param layer_protocol_name: The layer_protocol_name of this ConnectionEndPoint.
        :type layer_protocol_name: str
        """
        allowed_values = ["OTSiA", "OCH", "OTU", "ODU", "ETH", "ETY", "DSR"]  # noqa: E501
        if layer_protocol_name not in allowed_values:
            raise ValueError(
                "Invalid value for `layer_protocol_name` ({0}), must be one of {1}"
                .format(layer_protocol_name, allowed_values)
            )

        self._layer_protocol_name = layer_protocol_name

    @property
    def connectivity_service_end_point(self) -> str:
        """Gets the connectivity_service_end_point of this ConnectionEndPoint.


        :return: The connectivity_service_end_point of this ConnectionEndPoint.
        :rtype: str
        """
        return self._connectivity_service_end_point

    @connectivity_service_end_point.setter
    def connectivity_service_end_point(self, connectivity_service_end_point: str):
        """Sets the connectivity_service_end_point of this ConnectionEndPoint.


        :param connectivity_service_end_point: The connectivity_service_end_point of this ConnectionEndPoint.
        :type connectivity_service_end_point: str
        """

        self._connectivity_service_end_point = connectivity_service_end_point

    @property
    def parent_node_edge_point(self) -> List[str]:
        """Gets the parent_node_edge_point of this ConnectionEndPoint.


        :return: The parent_node_edge_point of this ConnectionEndPoint.
        :rtype: List[str]
        """
        return self._parent_node_edge_point

    @parent_node_edge_point.setter
    def parent_node_edge_point(self, parent_node_edge_point: List[str]):
        """Sets the parent_node_edge_point of this ConnectionEndPoint.


        :param parent_node_edge_point: The parent_node_edge_point of this ConnectionEndPoint.
        :type parent_node_edge_point: List[str]
        """

        self._parent_node_edge_point = parent_node_edge_point

    @property
    def client_node_edge_point(self) -> List[str]:
        """Gets the client_node_edge_point of this ConnectionEndPoint.


        :return: The client_node_edge_point of this ConnectionEndPoint.
        :rtype: List[str]
        """
        return self._client_node_edge_point

    @client_node_edge_point.setter
    def client_node_edge_point(self, client_node_edge_point: List[str]):
        """Sets the client_node_edge_point of this ConnectionEndPoint.


        :param client_node_edge_point: The client_node_edge_point of this ConnectionEndPoint.
        :type client_node_edge_point: List[str]
        """

        self._client_node_edge_point = client_node_edge_point

    @property
    def connection_port_direction(self) -> str:
        """Gets the connection_port_direction of this ConnectionEndPoint.

        The orientation of defined flow at the EndPoint.  # noqa: E501

        :return: The connection_port_direction of this ConnectionEndPoint.
        :rtype: str
        """
        return self._connection_port_direction

    @connection_port_direction.setter
    def connection_port_direction(self, connection_port_direction: str):
        """Sets the connection_port_direction of this ConnectionEndPoint.

        The orientation of defined flow at the EndPoint.  # noqa: E501

        :param connection_port_direction: The connection_port_direction of this ConnectionEndPoint.
        :type connection_port_direction: str
        """
        allowed_values = ["BIDIRECTIONAL", "INPUT", "OUTPUT", "UNIDENTIFIED_OR_UNKNOWN"]  # noqa: E501
        if connection_port_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_port_direction` ({0}), must be one of {1}"
                .format(connection_port_direction, allowed_values)
            )

        self._connection_port_direction = connection_port_direction

    @property
    def connection_port_role(self) -> str:
        """Gets the connection_port_role of this ConnectionEndPoint.

        Each EP of the FC has a role (e.g., working, protection, protected, symmetric, hub, spoke, leaf, root)  in the context of the FC with respect to the FC function.   # noqa: E501

        :return: The connection_port_role of this ConnectionEndPoint.
        :rtype: str
        """
        return self._connection_port_role

    @connection_port_role.setter
    def connection_port_role(self, connection_port_role: str):
        """Sets the connection_port_role of this ConnectionEndPoint.

        Each EP of the FC has a role (e.g., working, protection, protected, symmetric, hub, spoke, leaf, root)  in the context of the FC with respect to the FC function.   # noqa: E501

        :param connection_port_role: The connection_port_role of this ConnectionEndPoint.
        :type connection_port_role: str
        """
        allowed_values = ["SYMMETRIC", "ROOT", "LEAF", "TRUNK", "UNKNOWN"]  # noqa: E501
        if connection_port_role not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_port_role` ({0}), must be one of {1}"
                .format(connection_port_role, allowed_values)
            )

        self._connection_port_role = connection_port_role
