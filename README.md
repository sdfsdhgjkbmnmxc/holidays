holidays
========

Питонья база данных рабочих/нерабочих дней.

```python
>>> from holidays import is_holiday
>>> is_holiday(datetime.datetime(2012, 1, 1))
True
>>> is_holiday(datetime.datetime(2012, 12, 25))
False
```