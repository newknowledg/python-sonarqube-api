#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_MEASURES_COMPONENT_ENDPOINT,
    API_MEASURES_COMPONENT_TREE_ENDPOINT,
    API_MEASURES_SEARCH_HISTORY_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeMeasures(RestClient):
    """
    SonarQube measures Operations
    """

    special_attributes_map = {"from_date": "from", "to_date": "to"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeMeasures, self).__init__(**kwargs)

    @GET(API_MEASURES_COMPONENT_ENDPOINT)
    def get_component_with_specified_measures(
        self,
        component,
        metricKeys,
        branch=None,
        pullRequest=None,
        additionalFields=None,
    ):
        """
        SINCE 5.4
        Return component with specified measures.

        :param component: Component key
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param additionalFields: Comma-separated list of additional fields that can be returned in the response.
          Possible values are for: metrics,periods
        :param metricKeys: Comma-separated list of metric keys. Possible values are for: ncloc,complexity,violations
        :return:
        """

    @GET(API_MEASURES_COMPONENT_TREE_ENDPOINT)
    def get_component_tree(
        self,
        component,
        metricKeys,
        branch=None,
        pullRequest=None,
        additionalFields=None,
        asc=None,
        metricPeriodSort=None,
        metricSort=None,
        metricSortFilter=None,
        p=None,
        ps=None,
        pullRequest=None,
        q=None,
        qualifiers=None,
        s=None,
        strategy=None,
    ):
        """
        SINCE 5.4
        Return component with specified measures.

        :param component: Component key
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param additionalFields: Comma-separated list of additional fields that can be returned in the response.
          Possible values are for: metrics,periods
        :param metricKeys: Comma-separated list of metric keys. Possible values are for: ncloc,complexity,violations
        :return:
        """

    @GET(API_MEASURES_SEARCH_HISTORY_ENDPOINT)
    def search_history(
        self,
        component,
        metrics,
        branch=None,
        pullRequest=None,
        p=None,
        ps=None,
        pullRequest=None,
        from=None,
        to=None,
    ):
        """
        SINCE 5.4
        Return component with specified measures.

        :param component: Component key
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param additionalFields: Comma-separated list of additional fields that can be returned in the response.
          Possible values are for: metrics,periods
        :param metricKeys: Comma-separated list of metric keys. Possible values are for: ncloc,complexity,violations
        :return:
        """
