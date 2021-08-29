import pytest

from service.api.calendar import Calendar
from service.api.feishu import FeiShu

calendar = Calendar()
def test_list_no_calendar():
    feishu = FeiShu()
    calendar = Calendar()
    calendar.set_feishu(feishu)
    calendar.delete_all()
    calendars = calendar.list()
    assert len(calendars) == 0


def test_list_multi_calendar():
    Calendar.delete_all()
    Calendar.create()
    calendars = Calendar.list()
    assert len(calendars) == 5


def test_list_mass_calendar():
    Calendar.delete_all()
    Calendar.create()
    calendars = Calendar.list()
    assert len(calendars) == 500


@pytest.mark.parametrize("page_size", [0, 49, 50, 51, 499, 500, 501])
def test_list_mass_calendar(page_size):
    Calendar.delete_all()
    Calendar.create()
    calendars = Calendar.list(page_size)
    assert len(calendars) == page_size


def test_create(summary,**kwargs):
    c = calendar.create(
        'yancey_test',
        'method':
    )


