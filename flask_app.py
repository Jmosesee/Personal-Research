from flask import Flask, g, render_template
from flask_cors import CORS
from scrape import scrape2
from database import log_interested, get_interests, log_keyword, get_unsorted
import urllib.parse

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/hello/')
def hello_world():
    return 'Hello new World!'

@app.route('/hello2/')
def hello_world2():
    return 'Hello, World2!'

# @app.route('/scrape/<Word>/')
# def scrape_route(Word):
#     global a_tags
#     url = "https://en.wikipedia.org/wiki/" + Word
#     a_tags = scrape(url)
#     for tag in a_tags:
#         log_keyword(tag['href'][6:].split('#')[0])
#     return '\n'.join([','.join([a_tag.text, a_tag['href'][6:].split('#')[0]]) for a_tag in a_tags])

@app.route('/wiki/<path>')
def rerender(path):
    url = "https://en.wikipedia.org/wiki/" + path
    log_interested(path, 1)
    # if 'scraped' in g:
    #     print('Got scraped')
    #     disinterest_preceding(g.scraped, path)
    # else:
    #     print('No scraped')
    scraped = scrape2(url)
    return render_template('research2.html',scraped=scraped)

@app.route('/scrape-all/')
def scrape_all():
    interests = get_interests()
    print (len(interests))
    for interest in interests:
        print (interest[0])
        url = "https://en.wikipedia.org/wiki/" + interest[0]
        a_tags = scrape(url)
        for tag in a_tags:
            href = tag.get('href')
            if href:
                log_keyword(urllib.parse.unquote(href[6:].split('#')[0]))
    return "Done"

@app.route('/interested/<Word>')
def interested(Word):
    return log_interested(Word, 1)

@app.route('/satisfied/<Word>')
def satisfied(Word):
    return log_interested(Word, 2)

@app.route('/not-interested/<Word>')
def not_interested(Word):
    return log_interested(Word, 0)

@app.route('/show-context/<rowNumber>')
def show_context(rowNumber):
    global a_tags
    return a_tags[int(rowNumber)].parent.text

@app.route('/interests/')
def interests():
    interests = get_interests()
    return render_template('interests2.html', interests=interests)

@app.route('/unsorted/')
def unsorted():
    unsorted = get_unsorted()
    print(unsorted[0])
    return '\n'.join([w[0] for w in unsorted])

@app.route('/sorted_recipes/')
def sorted_recipes():
    recipes = get_recipes()
    return render_template('sorted_recipes.html', recipes=recipes)

@app.teardown_appcontext
def close_db(error):
    """Closes the database at the end of the request."""
    if hasattr(g, 'connection'):
        # print ("Disconnecting")       
        g.connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')