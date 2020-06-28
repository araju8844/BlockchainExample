#Imports
from uuid import uuid4
from flask import Flask, jsonify, request
import routes
#create a new Flask server pass in the name value of your local host
app = Flask(__name__)

#save my ip in node identifier
node_identifier = str(uuid4()).replace("-",'')

# create a Blockchain Application
blockchain = Blockchain()

#Register our API routes

#arguments for application to run
#checks if you are running the main file
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    #Usage: python main.py --port(any port number) ---> how we will connect to servers
    parser.add_argument("-p", "--port",default=3000, type=int, help="port to listen on")
    
    #gets the arguments from previous port statement
    args = parser.parse_args()
    port = args.port

    #run this on local host
    app.run(host="0.0.0.0",port=port)