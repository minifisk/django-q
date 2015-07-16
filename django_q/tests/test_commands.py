import pytest
from django.core.management import call_command


@pytest.mark.django_db
def test_qcluster():
    call_command('qcluster', run_once=True)


def test_qmonitor():
    call_command('qmonitor', run_once=True)
