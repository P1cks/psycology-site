from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('hello.html')


@app.route('/<int:quest>')
def asking(quest):
	return render_template('question.html', title='Questions', quest=quest)


if __name__ == '__main__':
	app.run(debug=True)