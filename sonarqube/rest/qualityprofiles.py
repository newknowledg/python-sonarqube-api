#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT,
    API_QUALITYPROFILES_SEARCH_ENDPOINT,
    API_QUALITYPROFILES_DELETE_ENDPOINT,
    API_QUALITYPROFILES_ACTIVATE_RULES_ENDPOINT,
    API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT,
    API_QUALITYPROFILES_BACKUP_ENDPOINT,
    API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT,
    API_QUALITYPROFILES_CHANGELOG_ENDPOINT,
    API_QUALITYPROFILES_COPY_ENDPOINT,
    API_QUALITYPROFILES_DEACTIVE_RULE_ENDPOINT,
    API_QUALITYPROFILES_DEACTIVE_RULES_ENDPOINT,
    API_QUALITYPROFILES_EXPORT_ENDPOINT,
    API_QUALITYPROFILES_EXPORTERS_ENDPOINT,
    API_QUALITYPROFILES_IMPORTERS_ENDPOINT,
    API_QUALITYPROFILES_INHERITANCE_ENDPOINT,
    API_QUALITYPROFILES_PROJECTS_ENDPOINT,
    API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT,
    API_QUALITYPROFILES_RENAME_ENDPOINT,
    API_QUALITYPROFILES_RESTORE_ENDPOINT,
    API_QUALITYPROFILES_CREATE_ENDPOINT,
    API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeQualityProfiles(RestClient):
    """
    SonarQube quality profiles Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeQualityProfiles, self).__init__(**kwargs)

    def activate_rule_for_quality_profile(
        self, key, rule, reset=False, severity=None, **params
    ):
        """
        SINCE 4.4
        Activate a rule for a given quality profile.

        :param key: Quality Profile key.
        :param rule: Rule key
        :param reset: Reset severity and parameters of activated rule.
          Set the values defined on parent profile or from rule default values.
        :param severity: Severity. Ignored if parameter reset is true.
          Possible values are for:
            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER
        :param params: customized parameters for the rule.Ignored if parameter reset is true.
        :return:
        """
        data = {"rule": rule, "key": key, "reset": reset and "true" or "false"}

        if not reset:
            # No reset, Add severity if given (if not default will be used?)
            if severity:
                data["severity"] = severity.upper()

            # Add params if we have any
            # Note: sort by key to allow checking easily
            params = ";".join(
                "{}={}".format(k, v) for k, v in sorted(params.items()) if v
            )
            if params:
                data["params"] = params

        return self._post(API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT, data=data)

    @GET(API_QUALITYPROFILES_SEARCH_ENDPOINT)
    def search_quality_profiles(
        self, organization=None, defaults="false", language=None, project=None, qualityProfile=None
    ):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_DELETE_ENDPOINT)
    def delete_quality_profile(self, language, qualityProfile, organization=None):
        """
        SINCE 5.2
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.
        :return:
        """

    @POST(API_QUALITYPROFILES_ACTIVATE_RULES_ENDPOINT)
    def activate_rules_for_quality_profile(
        self, activation=None, active_severities=None, asc=None, available_since=None, cwe=None,
        inheritence=None, is_template=None, languages=None, owaspTop10=None, q=none, qprofile=None,
        rule_key=None, s=None, sansTop25=None, severities=None, sonarsourceSecurity, statuses=None,
        tags=None, targetKey, targetSeverity=None, template_key=None, types=None
    ):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT)
    def add_project(self, language, project, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_BACKUP_ENDPOINT)
    def backup_quality_profile(self, language, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT)
    def change_parent(self, language, parentQualityProfile=None, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_CHANGELOG_ENDPOINT)
    def get_changelog(self, language, p=None, ps=None, since=None, to=None, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_COPY_ENDPOINT)
    def copy_quality_profile(self, fromKey, toName):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_CREATE_ENDPOINT)
    def create_quality_profile(self, language, name):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_DEACTIVE_RULE_ENDPOINT)
    def deactivate_rule_for_quality_profile(self, key, rule):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_DEACTIVE_RULES_ENDPOINT)
    def deactivate_rules_for_quality_profile(
        self, activation=None, active_severities=None, asc=None, available_since=None, cwe=None,
        inheritence=None, is_template=None, languages=None, owaspTop10=None, q=none, qprofile=None,
        rule_key=None, s=None, sansTop25=None, severities=None, sonarsourceSecurity, statuses=None,
        tags=None, targetKey, targetSeverity=None, template_key=None, types=None
    ):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_DELETE_ENDPOINT)
    def delete_quality_profile(self, language, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_EXPORT_ENDPOINT)
    def export_quality_profile(self, language, qualityProfile=None, exporterKey=None):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_EXPORTERS_ENDPOINT)
    def get_exporters(self):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_EXPORTERS_ENDPOINT)
    def get_exporters(self):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_IMPORTERS_ENDPOINT)
    def get_importers(self):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_INHERITANCE_ENDPOINT)
    def get_inheritance(self, language, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_PROJECTS_ENDPOINT)
    def get_projects(self, key, p=None, ps=None, q=None, selected=None):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT)
    def remove_project(self, language, project, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_RENAME_ENDPOINT)
    def rename_quality_profile(self, key, name):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_RESTORE_ENDPOINT)
    def restore_quality_profile(self, backup):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT)
    def set_default_quality_profile(self, language, qualityProfile):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

