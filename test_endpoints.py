import pytest
import requests

url = 'http://127.0.0.1:5000'

# Check '/' route and validate 200 response
def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 200

# Check '/games' route and validate 200 response
# Check for content type
# Check for presence of sample data
def test_get_all_games():
    r = requests.get(url+'/games')
    assert r.status_code == 200
    assert r.headers["Content-Type"] == "text/html; charset=utf-8"
    data = r.text
    assert len(data[0]) != 0
    assert data.__contains__('OMNO')

# Check '/games/<title>' route with valid tag and validate 200 response
# Check for presence of sample data
def test_individual_game():
    r = requests.get(url+'/games/OMNO')
    assert r.status_code == 200
    data = r.text
    assert data.__contains__('OMNO')

# Check '/games/<title>' route with invalid tag and validate 200 response
# Check for presence of sample data
def test_wrong_game_title():
    r = requests.get(url + '/games/wrong title')
    assert r.status_code == 200
    data = r.text
    assert data.__contains__('Not a valid title!')