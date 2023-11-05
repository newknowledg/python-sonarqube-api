#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_SETTINGS_LIST_DEFINITIONS_ENDPOINT,
    API_SETTINGS_RESET_ENDPOINT,
    API_SETTINGS_SET_ENDPOINT,
    API_SETTINGS_VALUES_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeSettings(RestClient):
    """
    SonarQube server Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeSettings, self).__init__(**kwargs)

    @GET(API_SERVER_VERSION_ENDPOINT)
    def get_server_version(self):
        """
        SINCE 2.10
        Version of SonarQube in plain text

        :return:
        """
