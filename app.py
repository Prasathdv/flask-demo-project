from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'job_title': 'DevOps Engineer',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'job_title': 'SRE',
  'location': 'Hyderabad, India',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 3,
  'job_title': 'Cloud Architect',
  'location': 'Chennai, India'
}, {
  'id': 4,
  'job_title': 'Cloud Engineer',
  'location': 'Gurgaon, India',
  'salary': 'Rs. 15,00,000'
}]


@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
