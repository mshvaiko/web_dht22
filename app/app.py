import threading
import time
from datetime import datetime

from dht import DHT22
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
dht22 = DHT22()

@app.route('/dht')
def temp():
    CURRENT_HUMIDITY, CURRENT_TEMPERATURE = dht22.get_dht()
    return render_template("dht.html", temperature=CURRENT_TEMPERATURE, humidity=CURRENT_HUMIDITY)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
