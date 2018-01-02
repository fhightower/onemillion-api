import onemillion
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/status', methods=['POST'])
def get_onemillion():
    if request.form['domain']:
        domain = request.form['domain']
        o = onemillion.OneMillion(cache_location='./cache', update=False)
        o.domain_in_million(domain)
        return "Ranking for {}: {}".format(domain, o.domain_in_million(domain))
    else:
        # TODO: make this a redirect rather than a render (1)
        return render_template("index.html", message="Please enter a domain.")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
