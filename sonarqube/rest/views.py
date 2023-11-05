#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.common import POST, GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_VIEWS_UPDATE_ENDPOINT,  # pro
    API_VIEWS_SHOW_ENDPOINT,  # pro
    API_VIEWS_LIST_ENDPOINT,  # pro
    API_VIEWS_ADD_APPLICATION_ENDPOINT,
    API_VIEWS_ADD_APPLICATION_BRANCH_ENDPOINT,
    API_VIEWS_ADD_PORTFOLIO_ENDPOINT ,
    API_VIEWS_ADD_PROJECT_ENDPOINT,
    API_VIEWS_ADD_PROJECT_BRANCH_ENDPOINT,
    API_VIEWS_APPLICATIONS_ENDPOINT,
    API_VIEWS_CREATE_ENDPOINT,
    API_VIEWS_DELETE_ENDPOINT,
    API_VIEWS_MOVE_ENDPOINT,
    API_VIEWS_MOVE_OPTIONS_ENDPOINT,
    API_VIEWS_PORTFOLIOS_ENDPOINT,
    API_VIEWS_REMOVE_APPLICATION_ENDPOINT,
    API_VIEWS_REMOVE_APPLICATION_BRANCH_ENDPOINT,
    API_VIEWS_REMOVE_PORTFOLIO_ENDPOINT,
    API_VIEWS_REMOVE_PROJECT_ENDPOINT,
    API_VIEWS_REMOVE_PROJECT_BRANCH_ENDPOINT,
    API_VIEWS_SET_MANUAL_MODE_ENDPOINT,
    API_VIEWS_SET_NONE_MODE_ENDPOINT,
    API_VIEWS_SET_NONE_MODE_ENDPOINT,
    API_VIEWS_SET_REGEXP_MODE_ENDPOINT,
    API_VIEWS_SET_REMAINING_PROJECTS_MODE_ENDPOINT,
    API_VIEWS_SET_TAGS_MODE_ENDPOINT,
)


class SonarQubeViews(RestClient):
    """
    Manage Portfolios
    """

    special_attributes_map = {"definition": "def"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeViews, self).__init__(**kwargs)

    def get_view(self, key):
        result = self.list()
        for view in result["views"]:
            if view["key"] == key:
                return view
    @GET(API_VIEWS_LIST)
    def list(self):
        """
        since 1.0
        List root portfolios.
        Requires authentication. Only portfolios with the admin permission are returned.

        :return:
        """
    @GET(API_VIEWS_SHOW)
    def show(self, key):
        """
        since 1.0
        Show the details of a portfolio, including its hierarchy and project selection mode.
        Authentication is required for this API endpoint

        :param key: The key of the portfolio
        :return:
        """

    @POST(API_VIEWS_UPDATE)
    def update(self, key, name, description=None):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_ADD_APPLICATION_ENDPOINT)
    def add_application(self, application, portfolio):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_ADD_APPLICATION_BRANCH_ENDPOINT)
    def add_application_branch(self, application, branch, key):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_ADD_PORTFOLIO_ENDPOINT)
    def add_portfolio(self, portfolio, reference):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_ADD_PROJECT_ENDPOINT)
    def add_project(self, key, project):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_ADD_PROJECT_BRANCH_ENDPOINT)
    def add_project_branch(self, branch, key, project):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @GET(API_VIEWS_APPLICATIONS_ENDPOINT)
    def get_applications(self,portfolio):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_CREATE_ENDPOINT)
    def create_portfolio(self, description=None, key=None, name, parent=None, visibilty=None):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_DELETE_ENDPOINT)
    def delete_portfolio(self, key):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_MOVE_ENDPOINT)
    def move_portfolio(self, destination, key):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @GET(API_VIEWS_MOVE_OPTIONS_ENDPOINT)
    def get_move_options(self, key):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @GET(API_VIEWS_PORTFOLIOS_ENDPOINT)
    def get_portfolios(self, portfolio):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_REMOVE_APPLICATION_ENDPOINT)
    def remove_application(self, application, portfolio):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_REMOVE_APPLICATION_BRANCH_ENDPOINT)
    def remove_application_branch(self, application, branch, key):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_REMOVE_PORTFOLIO_ENDPOINT)
    def remove_portfolio(self, portfolio, reference):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_REMOVE_PROJECT_ENDPOINT)
    def remove_project(self, key, project):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_REMOVE_PROJECT_BRANCH_ENDPOINT)
    def remove_project_branch(self, branch, key, project):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_SET_MANUAL_MODE_ENDPOINT)
    def set_manual_mode(self, portfolio):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_SET_NONE_MODE_ENDPOINT)
    def set_none_mode(self, portfolio):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_SET_REGEXP_MODE_ENDPOINT)
    def set_regexp_mode(self, branch, portfolio, regexp):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_SET_REMAINING_PROJECTS_MODE_ENDPOINT)
    def set_remaining_projects_mode(self, branch=None, portfolio):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_SET_TAGS_MODE_ENDPOINT)
    def set_tags_mode(self, branch=None, portfolio, tags):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

