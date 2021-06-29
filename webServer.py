from flask import Flask, request, render_template
from getResponse import getResponse

app = Flask(__name__)

key = 0


@app.route('/', methods=['GET'])  # do I need the squackets with only one method?
def hello():
    return render_template('form.html')


@app.route('/search_results', methods=['POST', 'GET'])
def searchResults():
    if request.method == 'GET':
        return f"The URL /search_results is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        search = request.form['Song']
        if(len(getResponse('search', 'term', search)) == 0):
            return render_template('error.html')
        else:
            hitList = getResponse('search', 'term', search)['tracks']['hits']
            return render_template('data.html', hitList=hitList)


@app.route('/recommendations', methods=['POST'])
def suggestions():
    key = int(request.form['Key'])
    if(len(getResponse('songs/list-recommendations', 'key', key)) == 0):
        return render_template('error.html')
    else:
        recommendations = getResponse('songs/list-recommendations', 'key', key)['tracks']
        return render_template('recommendations.html', recommendations=recommendations)
