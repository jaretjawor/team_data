from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    teams = []
    with open('team.data.esv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            teams.append(row)
    return render_template('index.html', teams=teams)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
