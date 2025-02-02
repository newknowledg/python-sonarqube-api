#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_CE_ACTIVITY_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeCe(RestClient):
    """
    SonarQube ce Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeCe, self).__init__(**kwargs)

    @GET(API_CE_ACTIVITY_ENDPOINT)
    def search_tasks(
        self,
        component=None,
        componentId=None,
        maxExecutedAt=None,
        minSubmittedAt=None,
        onlyCurrents=None,
        p=None,
        ps=None,
        q=None,
        status=None,
        type=None,
    ):
        """
        SINCE 5.2
        Search for tasks.

        :param component: Key of the component (project) to filter on (since 8.0)
        :param componentId: Id of the component (project) to filter on
        :param maxExecutedAt: Maximum date of end of task processing (inclusive)
        :param minSubmittedAt: Minimum date of task submission (inclusive)
        :param onlyCurrents: Filter on the last tasks (only the most recent finished task by project).
          default value is false.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 1000
        :param q: Limit search to:

          * component names that contain the supplied string
          * component keys that are exactly the same as the supplied string
          * task ids that are exactly the same as the supplied string

            Must not be set together with componentId
        :param status: Comma separated list of task statuses. Possible values are for:

          * SUCCESS
          * FAILED
          * CANCELED
          * PENDING
          * IN_PROGRESS

          default value is SUCCESS,FAILED,CANCELED
        :param type: Task type. Possible values:
          * REPORT
          * ISSUE_SYNC
          * APP_REFRESH
          * PROJECT_EXPORT
          * PROJECT_IMPORT
          * VIEW_REFRESH

        :return:
        """

    @GET(API_CE_ACTIVITY_STATUS_ENDPOINT)
    def get_activity_status(
        self,
        component=None
    ):
        """
        SINCE 5.2
        Search for tasks.

        :return:
        """

    @GET(API_CE_ACTIVITY_STATUS_ENDPOINT)
    def get_component(
        self,
        component=None
    ):
        """
        SINCE 5.2
        Search for tasks.

        :return:
        """

    @GET(API_CE_TASK_ENDPOINT)
    def get_task(
        self,
        additionalFields=None,
        id
    ):
        """
        SINCE 5.2
        Search for tasks.

        :return:
        """
