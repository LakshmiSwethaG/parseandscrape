# Parsing Metacritic Test

```
$ python api.py
```
Open http://127.0.0.1:5000/ for checking


## URLs
Base URL or to display top games: 
1. http://127.0.0.1:5000/
2. http://127.0.0.1:5000/games
3. http://127.0.0.1:5000/games/

URL for displaying one game at a time:
1. Click `title` in above urls or
2. http://127.0.0.1:5000/`<title>`


## Project structure
Code that returns response from Flask server:

    ├── api
    │   ├── api.py

Code for parsing the given url to fetch top games:

    │   ├── parseandscrape.py

Code for unit test cases:

    │   ├── test_endpoints.py

Code for html pages:

    │   ├── templates
    │   │   ├── main.html
    │   │   ├── index.html
    │   │   ├── result.html

All project dependencies installed by `pip`

    │   ├── requirements.txt


## Running unit tests
Run `$ python api.py` in one terminal and run the following command in other terminal in project path:

```sh
$ pytest -v
```






