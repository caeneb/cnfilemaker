import pytest
import pyfm.JDBCConnect as pyfm
from dotenv import dotenv_values

env = dotenv_values('test.env')

fm = pyfm.FileMaker(
    driver='fmjdbc.jar',
    server=env['server'],
    database=env['database'],
    username=env['username'],
    password=env['password']
)


def test_filemaker():
    fm.cursor.execute('SELECT name_first, name_last FROM test_db')
    results = fm.cursor.fetchall()
    assert results[0] == ('marcus', 'evans')


def test_select():
    results = fm.select('SELECT name_first, name_last FROM test_db')
    assert results[0] == ('marcus', 'evans')

    results = fm.select('SELECT name_first, name_last FROM test_db WHERE name_first = ?', ['jane'])
    assert results[0] == ('jane', 'doe')


def test_execute():
    fm.execute("INSERT INTO test_db (name_first, name_last) VALUES ('George', 'Washington')")
    results = fm.select(
        'SELECT name_first, name_last FROM test_db WHERE name_first = ? and name_last = ?', ['George', 'Washington']
    )
    assert results[0] == ('George', 'Washington')
    fm.execute('DELETE FROM test_db WHERE name_first = ? and name_last = ?', ['George', 'Washington'])
    results = fm.select(
        'SELECT name_first, name_last FROM test_db WHERE name_first = ? and name_last = ?', ['George', 'Washington']
    )
    assert results == []
