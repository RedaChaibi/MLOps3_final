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

def test__password_without_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abcd,;:!'))
    assert get_password_from_input() is None

def test__password_without_special_character(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abcd1234'))
    assert get_password_from_input() is None

def test__password_without_letter(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1234!&:;'))
    assert get_password_from_input() is None

def test__password_less_than_eight(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a1&'))
    assert get_password_from_input() is None

def test__password_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abcd!96&'))
    assert get_password_from_input() == 'Abcd!96&'