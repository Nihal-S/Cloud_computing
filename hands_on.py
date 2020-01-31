from flask import Flask, render_template,\
jsonify,request,abort

app=Flask(__name__)

#dictionary containing book names
# and quantities
catalog={}
catalog["book1"]=5
catalog["book2"]=4

#URL Routing:
@app.route('/hello/<name>')
def hello_world(name):	
	return "Hello, %s !" % name

#default method is GET
@app.route("/books")
def list_books():
	return jsonify(list(catalog.keys()))

@app.route("/borrow",methods=["POST"])
def borrow_book():
	#access book name sent as JSON object 
	#in POST request body
	book=request.get_json()["book"]
	if(catalog[book]>0):
		catalog[book]=catalog[book]-1
	return jsonify(catalog)


if __name__ == '__main__':	
	app.debug=True
	app.run()