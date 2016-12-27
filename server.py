from chess960 import generatePosition
from flask import Flask

app = Flask(__name__)

HTML_CODES = {"K": "&#9812;", "Q": "&#9813;", "R": "&#9814;", "B": "&#9815;", "N": "&#9816;"}

def positionIntoHTML(layout):
	newLayout = []
	
	for piece in layout:
		newLayout.append(HTML_CODES[piece])
	
	return newLayout


@app.route("/")
@app.route("/<int:number>/")
def index(number=1):
	html = "<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>Chess 960</title><style>td,th {padding: 0.5em; font-family: sans-serif; font-size: 20px; border-bottom: 1px solid black} td:not(:first-child) {font-size: 32px} tbody tr:nth-child(odd) {background: #e3e3e3; }</style></head><body><table><thead><tr><th>#</th>"
	
	for letter in ["a", "b", "c", "d", "e", "f", "g", "h"]:
		html += "<th>{}</th>".format(letter)
	
	html += "</thead><tbody>"
	
	for i in range(number):
		layout = positionIntoHTML(generatePosition())
		
		html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(str(i+1), *layout)
	
	html += "</tbody></table></body></html>"
	
	return html


app.run(host="0.0.0.0")