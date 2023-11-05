#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_USERS_SEARCH_ENDPOINT,
    API_USERS_ANONYMIZE_ENDPOINT,
    API_USERS_CHANGE_PASSWORD_ENDPOINT,
    API_USERS_CREATE_ENDPOINT,
    API_USERS_DEACTIVATE_ENDPOINT,
    API_USERS_GROUPS_ENDPOINT,
    API_USERS_UPDATE_ENDPOINT,
    API_USERS_UPDATE_IDENTITY_PROVIDER_ENDPOINT,
    API_USERS_UPDATE_LOGIN_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeUsers(RestClient):
    """
    SonarQube users Operations
    """

    MAX_SEARCH_NUM = 200

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeUsers, self).__init__(**kwargs)

    def get_user(self, login):
        result = self.search_users(q=login)
        users = result.get("users", [])

        for user in users:
            if user["login"] == login:
                return user

    @GET(API_USERS_SEARCH_ENDPOINT)
    def search_users(self, q=None, p=None, ps=None):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_USERS_ANONYMIZE_ENDPOINT)
    def anonymize_user(self, login):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_USERS_CHANGE_PASSWORD_ENDPOINT)
    def change_password(self, login, password, previousPassword=None):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_USERS_CREATE_ENDPOINT)
    def create_user(self, email=None, local=None, login, name, password=None, scmAccount=None):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_USERS_DEACTIVATE_ENDPOINT)
    def deactivate_user(self, anonymize=None, login):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @GET(API_USERS_GROUPS_ENDPOINT)
    def get_groups(self, login, p=None, ps=None, q=None, selected=None):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_USERS_UPDATE_ENDPOINT)
    def update_user(self, email=None, login, name=None, scmAccount=None):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_USERS_UPDATE_IDENTITY_PROVIDER_ENDPOINT)
    def update_identity_provider(self, login, newExternalIdentity=None, newExternalProvider):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_USERS_UPDATE_LOGIN_ENDPOINT)
    def update_user_login(self, login, newLogin):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """
