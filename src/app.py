

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
import datetime
import socket  
 


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/v1/details')
# ‘/’ URL is bound with hello_world() function.
def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, Leo boy!!'
    })



@app.route('/api/v1/healthz')
# ‘/’ URL is bound with hello_world() function.
def health():
    return jsonify({ 'status': 'Up'}), 200


@app.route('/api/v1/hello')
# ‘/’ URL is bound with hello_world() function.
def hello():
    return "Con mi burrito Sabaneroooo voy camino a Beleen :-) --> With new helf-hosted runners"



# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0")



