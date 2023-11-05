#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_ISSUES_SEARCH_ENDPOINT,
    API_ISSUES_ASSIGN_ENDPOINT,
    API_ISSUES_ADD_COMMENT_ENDPOINT,
    API_ISSUES_AUTHORS_ENDPOINT,
    API_ISSUES_BULK_CHANGE_ENDPOINT,
    API_ISSUES_CHANGELOG_ENDPOINT,
    API_ISSUES_DELETE_COMMENT_ENDPOINT,
    API_ISSUES_EDIT_COMMENT_ENDPOINT,
    API_ISSUES_DO_TRANS_ENDPOINT,
    API_ISSUES_REINDEX_ENDPOINT,
    API_ISSUES_SEVERITY_ENDPOINT,
    API_ISSUES_SET_TAGS_ENDPOINT,
    API_ISSUES_SET_TYPE_ENDPOINT,
    API_ISSUES_TAGS_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeIssues(RestClient):
    """
    SonarQube issues Operations
    """

    MAX_SEARCH_NUM = 100

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeIssues, self).__init__(**kwargs)

    def get_issue(self, key):
        result = self.search_issues(issues=key)
        issues = result.get("issues", [])

        for issue in issues:
            if issue["key"] == key:
                return issue

    @GET(API_ISSUES_SEARCH_ENDPOINT)
    def search_issues(
        self,
        organization=None,
        componentKeys=None,
        branch=None,
        pullRequest=None,
        additionalFields=None,
        asc="true",
        assigned=None,
        assignees=None,
        author=None,
        createdAfter=None,
        createdAt=None,
        createdBefore=None,
        createdInLast=None,
        cwe=None,
        facets=None,
        issues=None,
        languages=None,
        onComponentOnly="false",
        owaspTop10=None,
        p=None,
        ps=None,
        resolutions=None,
        resolved=None,
        rules=None,
        s=None,
        sansTop25=None,
        severities=None,
        sinceLeakPeriod="false",
        sonarsourceSecurity=None,
        statuses=None,
        tags=None,
        types=None,
    ):
        """
        SINCE 3.6
        Search for issues.

        :param organization: Organization key
        :param componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
            components (and all its descendants). A component can be a portfolio, project, module, directory or file.
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param additionalFields: Comma-separated list of the optional fields to be returned in response. Possible values are for:

            * _all
            * comments
            * languages
            * actionPlans
            * rules
            * transitions
            * actions
            * users

        :param asc: Ascending sort. Possible values are for: true, false, yes, no.default value is true
        :param assigned: To retrieve assigned or unassigned issues. Possible values are for: true, false, yes, no
        :param assignees: Comma-separated list of assignee logins. The value '__me__' can be used as a placeholder
            for user who performs the request
        :param author: SCM accounts. To set several values, the parameter must be called once for each value.
        :param componentKeys: Comma-separated list of component keys. Retrieve issues associated to a specific list of
            components (and all its descendants). A component can be a portfolio, project, module, directory or file.
        :param createdAfter: To retrieve issues created after the given date (inclusive).
            Either a date (server timezone) or datetime can be provided.
            If this parameter is set, createdSince must not be set
        :param createdBefore: To retrieve issues created before the given date (inclusive).
            Either a date (server timezone) or datetime can be provided.
        :param createdAt: Datetime to retrieve issues created during a specific analysis
        :param createdInLast: To retrieve issues created during a time span before the current time (exclusive).
            Accepted units are 'y' for year, 'm' for month, 'w' for week and 'd' for day. If this parameter is set,
            createdAfter must not be set.such as: 1m2w (1 month 2 weeks)
        :param cwe: Comma-separated list of CWE identifiers. Use 'unknown' to select issues not associated to any CWE.
        :param facets: Comma-separated list of the facets to be computed. No facet is computed by default. Possible values are for:

            * projects
            * moduleUuids
            * fileUuids
            * assigned_to_me
            * severities
            * statuses
            * resolutions
            * rules
            * assignees
            * authors
            * author
            * directories
            * languages
            * tags
            * types
            * owaspTop10
            * sansTop25
            * cwe
            * createdAt
            * sonarsourceSecurity

        :param issues: Comma-separated list of issue keys
        :param languages: Comma-separated list of languages. such as: java,js
        :param onComponentOnly: Return only issues at a component's level, not on its descendants (modules, directories,
            files, etc). This parameter is only considered when componentKeys or componentUuids is set. Possible values are for: true,
            false, yes, no. default value is false.
        :param owaspTop10: Comma-separated list of OWASP Top 10 lowercase categories.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param resolutions: Comma-separated list of resolutions.Possible values are for:

            * FALSE-POSITIVE
            * WONTFIX
            * FIXED
            * REMOVED

        :param resolved: To match resolved or unresolved issues. Possible values are for: true, false, yes, no
        :param rules: Comma-separated list of coding rule keys. Format is <repository>:<rule>.such as: squid:AvoidCycles
        :param s: Sort field. Possible values are for:

            * CREATION_DATE
            * UPDATE_DATE
            * CLOSE_DATE
            * ASSIGNEE
            * SEVERITY
            * STATUS
            * FILE_LINE

        :param sansTop25: Comma-separated list of SANS Top 25 categories. Possible values are for:

            * insecure-interaction
            * risky-resource
            * porous-defenses

        :param severities: Comma-separated list of severities.Possible values are for:

            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER

        :param sinceLeakPeriod: To retrieve issues created since the leak period.If this parameter is set to
            a truthy value, createdAfter must not be set and one component id or key must be provided.
            Possible values are for: true, false, yes, no. default value is false.
        :param sonarsourceSecurity: Comma-separated list of SonarSource security categories. Use 'others' to
            select issues not associated with any category。Possible values are for:

            * sql-injection
            * command-injection
            * path-traversal-injection
            * ldap-injection
            * xpath-injection
            * rce
            * dos
            * ssrf
            * csrf
            * xss
            * log-injection
            * http-response-splitting
            * open-redirect
            * xxe
            * object-injection
            * weak-cryptography
            * auth
            * insecure-conf
            * file-manipulation
            * others

        :param statuses: Comma-separated list of statuses.Possible values are for:

            * OPEN
            * CONFIRMED
            * REOPENED
            * RESOLVED
            * CLOSED
            * TO_REVIEW
            * IN_REVIEW
            * REVIEWED

        :param tags: Comma-separated list of tags.such as: security,convention
        :param types: Comma-separated list of types.Possible values are for:

            * CODE_SMELL
            * BUG
            * VULNERABILITY

        :return:
        """

    @POST(API_ISSUES_ASSIGN_ENDPOINT)
    def issue_assign(self, issue, assignee=None):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_ADD_COMMENT_ENDPOINT)
    def add_comment(self, issue, text):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @GET(API_ISSUES_AUTHORS_ENDPOINT)
    def search_authors(self, project=None, ps=None, q=None):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_BULK_CHANGE_ENDPOINT)
    def bulk_change(self, add_tags=None, assign=None, comment=None, do_transition=None, issues, remove_tags=None, sendNotification=None, set_severity=None, set_type=None):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @GET(API_ISSUES_CHANGELOG_ENDPOINT)
    def get_changelog(self, issues):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_DELETE_COMMENT_ENDPOINT)
    def delete_comment(self, comment):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_DO_TRANS_ENDPOINT)
    def do_transition(self, issue, transition):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_EDIT_COMMENT_ENDPOINT)
    def edit_comment(self, comment, text):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_REINDEX_ENDPOINT)
    def reindex(self, project):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_SEVERITY_ENDPOINT)
    def set_severity(self, issue, severity):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_SET_TAGS_ENDPOINT)
    def set_tags(self, issue, tags=None):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @POST(API_ISSUES_SET_TYPE_ENDPOINT)
    def set_type(self, issue, type):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """

    @GET(API_ISSUES_TAGS_ENDPOINT)
    def list_tags(self, all=None, branch=None, ps=None, q=None):
        """
        SINCE 3.6
        Assign/Unassign an issue

        :param issue: Issue key
        :param assignee: Login of the assignee. When not set, it will unassign the issue. Use '_me' to
          assign to current user
        :return: request response
        """
