# -*- coding: utf-8 -*-

from resolver.date import DateResolver
from datetime import datetime


class TestDateResolver(object):

    def setup_method(self, test_method):
        self.file_contents_resolver = DateResolver(
            argument=None
        )

    def test_resolving_with_valid_format(self):
        format = "%m/%d/%Y"
        expected_date = datetime.now().strftime(format)

        self.file_contents_resolver.argument = format
        result = self.file_contents_resolver.resolve()
        assert result == expected_date

    # invalid input will result in date in default format
    def test_resolving_with_invalid_format(self):
        format = ""
        expected_date = datetime.now().strftime(format)

        self.file_contents_resolver.argument = "invalid"
        result = self.file_contents_resolver.resolve()
        assert result[:10] != expected_date[:10]
