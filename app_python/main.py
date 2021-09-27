import datetime

from flask import Flask
import pytz


app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_time():
    """
    This method firstly sets the timezone for tz_moscow then extracts from it the current time using standard datetime,
    formats time to the template and returns the resulting string.
    :return: {string} current time
    """
    count = 0
    with open("./volumes/count", "r") as f:
        count = int(f.read()) + 1
    with open("./volumes/count", "w") as f:
        f.write(str(count))

    tz_moscow = pytz.timezone('Europe/Moscow')
    datetime_moscow = datetime.datetime.now(tz_moscow)
    server_time = datetime_moscow.strftime('%A %B, %d %Y %H:%M:%S')
    return "server time {}".format(server_time)

@app.route("/visits", methods=['GET'])
def get_count():
    """
    Shows the visits' counter
    """
    count = 0
    with open("./volumes/count", "r") as f:
        count = int(f.read())
    return "visits {}".format(count)