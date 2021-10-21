# Expose a REST API for retrieving top PS4 games
import flask
from flask import render_template
from parseandscrape import topps4games

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# A HTTP "GET" request a "/games" returns all top PS4 games on metacritic page
@app.route('/', methods=['GET'])
@app.route('/games', methods=['GET'])
@app.route('/games/', methods=['GET'])
def api_all():
    return render_template('index.html', games=topps4games)


# A HTTP "GET" request at "/games/TITLE_OF_GAME_GOES_HERE" returns JSON for a specific job 
@app.route('/games/<string:title>', methods=['GET'])
def returnOne(title = None):
    # Create an empty list for our results
    # Loop through the data and match results that fit the requested title.
    for res in topps4games:
        if res['title'] == title:
           return render_template('result.html', result=res)
    return render_template('result.html', result=None)


app.run(use_reloader=True)