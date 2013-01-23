# -*- coding:utf-8 -*-

class Holidays(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def get_min_year(self):
        return self.cfg.min_year

    def get_max_year(self):
        return self.cfg.max_year

    def is_holiday(self, dt):
        if not self.cfg.min_year <= dt.year <= self.cfg.max_year:
            raise ValueError(dt.year)

        datetuple = (dt.year, dt.month, dt.day)
        if datetuple in self.cfg.force_workdays:
            return False
        elif datetuple in self.cfg.force_holidays:
            return True
        else:
            return dt.isoweekday() >= 6
