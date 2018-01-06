from flask import flash, Flask, render_template, redirect, request, url_for
import onemillion

app = Flask(__name__)
app.secret_key = 'abc'


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/onemillion', methods=['POST'])
def get_onemillion():
    if request.form['domain']:
        domain = request.form['domain']
        return redirect(url_for('show_onemillion', domain=domain))
    else:
        flash('Please enter a domain.', 'error')
        return redirect(url_for('index'))


@app.route('/onemillion/<domain>')
def show_onemillion(domain):
    o = onemillion.OneMillion(cache_location='./cache', update=False)
    return "{}".format(o.domain_in_million(domain))


if __name__ == '__main__':
    app.run()
