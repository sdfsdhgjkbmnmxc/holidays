# -*- coding:utf-8 -*-

min_year = 2012
max_year = 2022

force_workdays = set((
  # 2013

  # 2012
  (2012, 3, 11),
  (2012, 4, 28),
  (2012, 5, 5),
  (2012, 6, 9),
  (2012, 12, 29),
))


force_holidays = set()

for year in range(min_year, max_year):
    force_holidays.update((
        # 1, 2, 3, 4, 5 января - Новогодние каникулы;
        (year, 1, 1), (year, 1, 2), (year, 1, 3), (year, 1, 4), (year, 1, 5),
        # 7 января — Рождество Христово;
        (year, 1, 7),
        # 23 февраля - День защитника Отечества;
        (year, 2, 23),
        # 8 марта - Международный женский день;
        (year, 3, 8),
        # 1 мая - Праздник Весны и Труда;
        (year, 5, 1),
        # 9 мая - День Победы;
        (year, 5, 9),
        # 12 июня - День России;
        (year, 6, 12),
        # 4 ноября - День народного единства.
        (year, 11, 4),
    ))

force_holidays.update((
  # 2013
  (2013, 1, 8),
  (2013, 5, 2), (2013, 5, 3), (2013, 5, 4), (2013, 5, 10),
  # 2012
  (2012, 1, 6), (2012, 1, 9),
  (2012, 3, 9),
  (2012, 4, 30),
  (2012, 5, 7), (2012, 5, 8),
  (2012, 6, 11), (2012, 6, 12),
  (2012, 11, 5),
  (2012, 12, 31),
))
