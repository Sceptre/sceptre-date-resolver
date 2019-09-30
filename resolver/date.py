# -*- coding: utf-8 -*-

import logging
import datetime

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
        Retrieves the current date.

        :returns: the current date
        :rtype: str
        """
        format = self.DEFAULT_FORMAT

        if self.argument:
            format = self.argument

        try:
            now = datetime.datetime.now()
            date = now.strftime(format)
            self.logger.debug("%s - date: %s",
                              self.stack.name, date)
        except ValueError as ve:
            self.logger.error("%s - Invalid date format: %s",
                              self.stack.name, format)
        except Exception as e:
            self.logger.error("%s - Failed to resolve date",
                              self.stack.name)
            raise e

        return date
