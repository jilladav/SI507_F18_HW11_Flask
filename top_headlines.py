from flask import Flask, render_template
from secrets import api_key
import requests
import datetime
app = Flask(__name__)

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'

@app.route('/user/<name>')
def get_headlines(name):

	base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
	params = {"api-key" : api_key}

	results = requests.get(base_url,params).json()

	top_results = results['results'][:5]
	headlines_list = []
	for result in top_results:
		headlines_list.append(result['title'] + " (" + result['url'] + ")")


	#I worked with Morgan Durow for this part of the EC	
	current_time = datetime.datetime.now().time()
	
	if int(str(current_time)[:2]) < 12:
		greeting = "morning"
	elif int(str(current_time)[:2]) >= 12 and int(str(current_time)[:2]) <= 16:
		greeting = "afternoon"
	elif int(str(current_time)[:2]) >= 16 and int(str(current_time)[:2]) <= 20:
		greeting = "evening"
	else:
		greeting = "night"


	return render_template('user.html', name=name, my_list=headlines_list, greeting=greeting)


@app.route('/user/<name>/<section>')
def get_headlines_for_section(name, section):
	params = {"api-key": api_key}
	base_url = "https://api.nytimes.com/svc/topstories/v2/" + section + ".json"

	results = requests.get(base_url, params).json()

	top_results = results['results'][:5]
	headlines_list = []
	for result in top_results:
		headlines_list.append(result['title'] + " (" + result['url'] + ")")


	#I worked with Morgan Durow for this part of the EC	
	current_time = datetime.datetime.now().time()
	
	if int(str(current_time)[:2]) < 12:
		greeting = "morning"
	elif int(str(current_time)[:2]) >= 12 and int(str(current_time)[:2]) <= 16:
		greeting = "afternoon"
	elif int(str(current_time)[:2]) >= 16 and int(str(current_time)[:2]) <= 20:
		greeting = "evening"
	else:
		greeting = "night"

	return render_template('section.html', name=name, my_list=headlines_list, section=section, greeting=greeting)

if __name__ == '__main__':    
	print('starting Flask app', app.name)    
	app.run(debug=True)
