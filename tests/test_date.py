# -*- coding: utf-8 -*-

import pytest

from resolver.date import Date
from datetime import datetime

class TestDateResolver(object):

    def setup_method(self, test_method):
        self.file_contents_resolver = Date(
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
        self.file_contents_resolver.argument = "invalid"
        result = self.file_contents_resolver.resolve()

    # none input will result in date with default format
    def test_resolving_with_none_format(self):
        self.file_contents_resolver.argument = None
        result = self.file_contents_resolver.resolve()
