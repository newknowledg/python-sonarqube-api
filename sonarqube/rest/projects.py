#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECTS_SEARCH_ENDPOINT,
    API_PROJECTS_BULK_DELETE_ENDPOINT,
    API_PROJECTS_CREATE_ENDPOINT,
    API_PROJECTS_DELETE_ENDPOINT,
    API_PROJECTS_EXPORT_FINDINGS_ENDPOINT,
    API_PROJECTS_LICENSE_USAGE_ENDPOINT,
    API_PROJECTS_UPDATE_KEY_ENDPOINT,
    API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeProjects(RestClient):
    """
    SonarQube projects Operations
    """

    special_attributes_map = {"previous_project_key": "from", "new_project_key": "to"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjects, self).__init__(**kwargs)

    def get_project(self, key, organization=None):
        result = self.search_projects(organization=organization, projects=key)
        projects = result.get("components", [])

        for project in projects:
            if project["key"] == key:
                return project

    @GET(API_PROJECTS_SEARCH_ENDPOINT)
    def search_projects(
        self,
        organization=None,
        analyzedBefore=None,
        onProvisionedOnly="false",
        projects=None,
        p=None,
        ps=None,
        q=None,
        qualifiers="TRK",
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :return:
        """

    @POST(API_PROJECTS_BULK_DELETE_ENDPOINT)
    def bulk_delete(
        self,
        mainBranch=None,
        name,
        projects,
        visibility=None,
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :return:
        """

    @POST(API_PROJECTS_DELETE_ENDPOINT)
    def delete(
        self,
        project,
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :return:
        """

    @GET(API_PROJECTS_EXPORT_FINDINGS_ENDPOINT)
    def export_findings(
        self,
        project,
        pullRequest=None
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :return:
        """

    @GET(API_PROJECTS_LICENSE_USAGE_ENDPOINT)
    def licecnse_usage(
        self,
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :return:
        """

    @POST(API_PROJECTS_UPDATE_KEY_ENDPOINT)
    def update_key(
        self,
        from,
        to,
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :return:
        """

    @POST(API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT)
    def update_visibility(
        self,
        project,
        visibility,
    ):
        """
        SINCE 6.3
        Search for projects or views to administrate them.

        :return:
        """
