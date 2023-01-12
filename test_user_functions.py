import pytest
import io
from user_functions import *

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

def test__user_name_with_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra adaltas'))
    assert get_user_name_from_input() is None

def test__user_name_with_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petraadaltas'))
    assert get_user_name_from_input() == 'petraadaltas'