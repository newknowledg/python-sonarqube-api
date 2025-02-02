#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_BADGES_MEASURE_ENDPOINT,
    API_PROJECT_BADGES_QUALITY_GATE_ENDPOINT,
    API_PROJECT_BADGES_TOKEN_ENDPOINT,
    API_PROJECT_BADGES_RENEW_TOKEN_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeProjectBadges(RestClient):
    """
    SonarQube project badges Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectBadges, self).__init__(**kwargs)

    @GET(API_PROJECT_BADGES_MEASURE_ENDPOINT)
    def generate_badge_for_project_measures(self, project, metric, branch=None, token=None):
        """
        SINCE 7.1
        Generate badge for project's measure as an SVG.

        :param project: Project or application key
        :param branch: Long living branch key
        :param metric: Metric key,
          Possible values are for:
            * bugs
            * code_smells
            * coverage
            * duplicated_lines_density
            * ncloc
            * sqale_rating
            * alert_status
            * reliability_rating
            * security_rating
            * sqale_index
            * vulnerabilities
        :param token: Security token
        :return:
        """

    @GET(API_PROJECT_BADGES_QUALITY_GATE_ENDPOINT)
    def generate_badge_for_project_quality_gate(self, project, branch=None, token=None):
        """
        SINCE 7.1
        Generate badge for project's measure as an SVG.

        :param project: Project or application key
        :param branch: Long living branch key
        :param metric: Metric key,
          Possible values are for:
            * bugs
            * code_smells
            * coverage
            * duplicated_lines_density
            * ncloc
            * sqale_rating
            * alert_status
            * reliability_rating
            * security_rating
            * sqale_index
            * vulnerabilities
        :param token: Security token
        :return:
        """

    @POST(API_PROJECT_BADGES_RENEW_TOKEN_ENDPOINT)
    def renew_token(self, project):
        """
        SINCE 7.1
        Generate badge for project's measure as an SVG.

        :param project: Project or application key
        :param branch: Long living branch key
        :param metric: Metric key,
          Possible values are for:
            * bugs
            * code_smells
            * coverage
            * duplicated_lines_density
            * ncloc
            * sqale_rating
            * alert_status
            * reliability_rating
            * security_rating
            * sqale_index
            * vulnerabilities
        :param token: Security token
        :return:
        """

    @GET(API_PROJECT_BADGES_TOKEN_ENDPOINT)
    def get_token(self, project):
        """
        SINCE 7.1
        Generate badge for project's measure as an SVG.

        :param project: Project or application key
        :param branch: Long living branch key
        :param metric: Metric key,
          Possible values are for:
            * bugs
            * code_smells
            * coverage
            * duplicated_lines_density
            * ncloc
            * sqale_rating
            * alert_status
            * reliability_rating
            * security_rating
            * sqale_index
            * vulnerabilities
        :param token: Security token
        :return:
        """
