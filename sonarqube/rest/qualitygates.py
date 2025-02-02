#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_QUALITYGATES_LIST_ENDPOINT,
    API_QUALITYGATES_SELECT_ENDPOINT,
    API_QUALITYGATES_SEARCH_ENDPOINT,
    API_QUALITYGATES_COPY_ENDPOINT,
    API_QUALITYGATES_CREATE_ENDPOINT,
    API_QUALITYGATES_CREATE_CONDITION_ENDPOINT,
    API_QUALITYGATES_DELETE_CONDITION_ENDPOINT,
    API_QUALITYGATES_DESELECT_ENDPOINT,
    API_QUALITYGATES_DESTROY_ENDPOINT,
    API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT,
    API_QUALITYGATES_PROJECT_STATUS_ENDPOINT,
    API_QUALITYGATES_RENAME_ENDPOINT,
    API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT,
    API_QUALITYGATES_SHOW_ENDPOINT,
    API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeQualityGates(RestClient):
    """
    SonarQube quality gates Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeQualityGates, self).__init__(**kwargs)

    @GET(API_QUALITYGATES_SEARCH_ENDPOINT)
    def get_qualitygate_projects(
        self, gateName, selected="selected", query=None, organization=None, page=None, pageSize=None
    ):
        """
        SINCE 4.3
        Search for projects associated (or not) to a quality gate.

        :param gateName: Quality Gate name. since 8.4
        :param selected: Depending on the value, show only selected items (selected=selected),
          deselected items (selected=deselected), or all items with their selection status (selected=all).
          Possible values are for:
            * all
            * deselected
            * selected
          default value is selected
        :param query: To search for projects containing this string.
          If this parameter is set, "selected" is set to "all".
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :param page: page number.
        :param pageSize: Page size.
        :return:
        """

    @GET(API_QUALITYGATES_LIST_ENDPOINT)
    def get_quality_gates(self, organization=None):
        """
        SINCE 4.3
        Get a list of quality gates

        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_SELECT_ENDPOINT)
    def select_quality_gate_for_project(self, projectKey, gateName, organization=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        :param projectKey: Project key
        :param gateName: Quality gate name (since version 8.4). Refer https://sonarqube.inria.fr/sonarqube/web_api/api/qualitygates
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_COPY_ENDPOINT)
    def copy(self, sourceName=None, name):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_CREATE_ENDPOINT)
    def create(self, name):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_CREATE_CONDITION_ENDPOINT)
    def create_condition(self, error, gateName=None, metric, op=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_DELETE_CONDITION_ENDPOINT)
    def delete_condition(self, id):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_DESELECT_ENDPOINT)
    def deselect(self, projectKey):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_DESTROY_ENDPOINT)
    def destroy(self, name=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @GET(API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT)
    def get_by_project(self, project):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @GET(API_QUALITYGATES_PROJECT_STATUS_ENDPOINT)
    def get_project_status(self, analysisId=None, branch=None, projectId=None, projectKey=None, PullRequest=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_RENAME_ENDPOINT)
    def rename(self, currentName=None, name):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT)
    def set_as_default(self, name=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @GET(API_QUALITYGATES_SHOW_ENDPOINT)
    def show_gate(self, id=None, name=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

    @POST(API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT)
    def uodate_condition(self, error, id, metric, op=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        """

