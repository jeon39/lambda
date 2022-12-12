# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.cloudwatch.cloudwatchalarmstatechange.ConfigurationItem import ConfigurationItem  # noqa: F401,E501

class Configuration(object):


    _types = {
        'metrics': 'list[ConfigurationItem]',
        'description': 'str',
        'alarmRule': 'str',
        'actionsSuppressor': 'str',
        'actionsSuppressorWaitPeriod': 'float',
        'actionsSuppressorExtensionPeriod': 'float'
    }

    _attribute_map = {
        'metrics': 'metrics',
        'description': 'description',
        'alarmRule': 'alarmRule',
        'actionsSuppressor': 'actionsSuppressor',
        'actionsSuppressorWaitPeriod': 'actionsSuppressorWaitPeriod',
        'actionsSuppressorExtensionPeriod': 'actionsSuppressorExtensionPeriod'
    }

    def __init__(self, metrics=None, description=None, alarmRule=None, actionsSuppressor=None, actionsSuppressorWaitPeriod=None, actionsSuppressorExtensionPeriod=None):  # noqa: E501
        self._metrics = None
        self._description = None
        self._alarmRule = None
        self._actionsSuppressor = None
        self._actionsSuppressorWaitPeriod = None
        self._actionsSuppressorExtensionPeriod = None
        self.discriminator = None
        self.metrics = metrics
        self.description = description
        self.alarmRule = alarmRule
        self.actionsSuppressor = actionsSuppressor
        self.actionsSuppressorWaitPeriod = actionsSuppressorWaitPeriod
        self.actionsSuppressorExtensionPeriod = actionsSuppressorExtensionPeriod


    @property
    def metrics(self):

        return self._metrics

    @metrics.setter
    def metrics(self, metrics):


        self._metrics = metrics


    @property
    def description(self):

        return self._description

    @description.setter
    def description(self, description):


        self._description = description


    @property
    def alarmRule(self):

        return self._alarmRule

    @alarmRule.setter
    def alarmRule(self, alarmRule):


        self._alarmRule = alarmRule


    @property
    def actionsSuppressor(self):

        return self._actionsSuppressor

    @actionsSuppressor.setter
    def actionsSuppressor(self, actionsSuppressor):


        self._actionsSuppressor = actionsSuppressor


    @property
    def actionsSuppressorWaitPeriod(self):

        return self._actionsSuppressorWaitPeriod

    @actionsSuppressorWaitPeriod.setter
    def actionsSuppressorWaitPeriod(self, actionsSuppressorWaitPeriod):


        self._actionsSuppressorWaitPeriod = actionsSuppressorWaitPeriod


    @property
    def actionsSuppressorExtensionPeriod(self):

        return self._actionsSuppressorExtensionPeriod

    @actionsSuppressorExtensionPeriod.setter
    def actionsSuppressorExtensionPeriod(self, actionsSuppressorExtensionPeriod):


        self._actionsSuppressorExtensionPeriod = actionsSuppressorExtensionPeriod

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Configuration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Configuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

