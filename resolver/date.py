# -*- coding: utf-8 -*-

import logging
from datetime import datetime

from sceptre.resolvers import Resolver


class Date(Resolver):
    """
    Resolves the current datetime.

    :param argument: The ISO 8601 date format:
            https://docs.python.org/3/library/time.html#time.strftime
    :type argument: str
    """

    DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        super(Date, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        Retrieves the current date in ISO 8601 format

        :returns: the current date
        :rtype: str
        """
        format = self.DEFAULT_FORMAT

        if self.argument:
            format = self.argument

        try:
            now = datetime.now()
            print("\nit's now: "+str(now))
            date = now.strftime(format)

        except Exception as e:
            raise e

        return date
