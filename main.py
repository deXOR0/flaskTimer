from flask import Flask, render_template, redirect
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def timer():
    target = '2020-08-03 06:29:10'  # change target to desired time
    now = datetime.now()
    if now >= datetime.strptime(target, '%Y-%m-%d %H:%M:%S'):
        # change this url to your desired url
        return redirect('https://www.youtube.com/')
    return render_template('timer.html', time=target)


if __name__ == '__main__':
    app.run(debug=True)
