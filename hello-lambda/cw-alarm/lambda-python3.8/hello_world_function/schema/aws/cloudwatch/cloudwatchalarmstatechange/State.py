# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class State(object):


    _types = {
        'reason': 'str',
        'reasonData': 'str',
        'value': 'str',
        'timestamp': 'str',
        'actionsSuppressedBy': 'str',
        'actionsSuppressedReason': 'str',
        'evaluationState': 'str'
    }

    _attribute_map = {
        'reason': 'reason',
        'reasonData': 'reasonData',
        'value': 'value',
        'timestamp': 'timestamp',
        'actionsSuppressedBy': 'actionsSuppressedBy',
        'actionsSuppressedReason': 'actionsSuppressedReason',
        'evaluationState': 'evaluationState'
    }

    def __init__(self, reason=None, reasonData=None, value=None, timestamp=None, actionsSuppressedBy=None, actionsSuppressedReason=None, evaluationState=None):  # noqa: E501
        self._reason = None
        self._reasonData = None
        self._value = None
        self._timestamp = None
        self._actionsSuppressedBy = None
        self._actionsSuppressedReason = None
        self._evaluationState = None
        self.discriminator = None
        self.reason = reason
        self.reasonData = reasonData
        self.value = value
        self.timestamp = timestamp
        self.actionsSuppressedBy = actionsSuppressedBy
        self.actionsSuppressedReason = actionsSuppressedReason
        self.evaluationState = evaluationState


    @property
    def reason(self):

        return self._reason

    @reason.setter
    def reason(self, reason):


        self._reason = reason


    @property
    def reasonData(self):

        return self._reasonData

    @reasonData.setter
    def reasonData(self, reasonData):


        self._reasonData = reasonData


    @property
    def value(self):

        return self._value

    @value.setter
    def value(self, value):


        self._value = value


    @property
    def timestamp(self):

        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):


        self._timestamp = timestamp


    @property
    def actionsSuppressedBy(self):

        return self._actionsSuppressedBy

    @actionsSuppressedBy.setter
    def actionsSuppressedBy(self, actionsSuppressedBy):


        self._actionsSuppressedBy = actionsSuppressedBy


    @property
    def actionsSuppressedReason(self):

        return self._actionsSuppressedReason

    @actionsSuppressedReason.setter
    def actionsSuppressedReason(self, actionsSuppressedReason):


        self._actionsSuppressedReason = actionsSuppressedReason


    @property
    def evaluationState(self):

        return self._evaluationState

    @evaluationState.setter
    def evaluationState(self, evaluationState):


        self._evaluationState = evaluationState

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
        if issubclass(State, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

