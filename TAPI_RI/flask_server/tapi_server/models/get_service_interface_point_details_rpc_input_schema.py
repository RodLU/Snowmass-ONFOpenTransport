# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class GetServiceInterfacePointDetailsRPCInputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sip_id_or_name: str=None):  # noqa: E501
        """GetServiceInterfacePointDetailsRPCInputSchema - a model defined in Swagger

        :param sip_id_or_name: The sip_id_or_name of this GetServiceInterfacePointDetailsRPCInputSchema.  # noqa: E501
        :type sip_id_or_name: str
        """
        self.swagger_types = {
            'sip_id_or_name': str
        }

        self.attribute_map = {
            'sip_id_or_name': 'sip-id-or-name'
        }

        self._sip_id_or_name = sip_id_or_name

    @classmethod
    def from_dict(cls, dikt) -> 'GetServiceInterfacePointDetailsRPCInputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get-service-interface-point-detailsRPC_input_schema of this GetServiceInterfacePointDetailsRPCInputSchema.  # noqa: E501
        :rtype: GetServiceInterfacePointDetailsRPCInputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sip_id_or_name(self) -> str:
        """Gets the sip_id_or_name of this GetServiceInterfacePointDetailsRPCInputSchema.


        :return: The sip_id_or_name of this GetServiceInterfacePointDetailsRPCInputSchema.
        :rtype: str
        """
        return self._sip_id_or_name

    @sip_id_or_name.setter
    def sip_id_or_name(self, sip_id_or_name: str):
        """Sets the sip_id_or_name of this GetServiceInterfacePointDetailsRPCInputSchema.


        :param sip_id_or_name: The sip_id_or_name of this GetServiceInterfacePointDetailsRPCInputSchema.
        :type sip_id_or_name: str
        """

        self._sip_id_or_name = sip_id_or_name
