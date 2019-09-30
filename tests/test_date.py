# -*- coding: utf-8 -*-

from resolver.date import DateResolver
from datetime import datetime
from mock import MagicMock
from sceptre.stack import Stack

class TestDateResolver(object):

    def setup_method(self, test_method):
        stack = MagicMock(spec=Stack)
        stack.name = "test"
        self.date_resolver = DateResolver(
            None, stack
        )

    def test_resolving_with_valid_format(self):
        format = "%m/%d/%Y"
        expected_date = datetime.now().strftime(format)

        self.date_resolver.argument = format
        result = self.date_resolver.resolve()
        assert result == expected_date

    # invalid input will result in date in default format
    def test_resolving_with_invalid_format(self):
        format = ""
        expected_date = datetime.now().strftime(format)

        self.date_resolver.argument = "invalid"
        result = self.date_resolver.resolve()
        assert result[:10] != expected_date[:10]
