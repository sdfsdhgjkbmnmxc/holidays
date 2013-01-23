from holidays.abstract import Holidays
from holidays import rf


_instance = Holidays(rf)
is_holiday = _instance.is_holiday
min_year = _instance.get_min_year()
max_year = _instance.get_max_year()
