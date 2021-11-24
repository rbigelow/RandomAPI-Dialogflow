import json
import random
from random import seed
from random import randint
from datetime import datetime
from chalice import Chalice

app = Chalice(app_name='RandomAPI')
#app.debug = True

#random.seed(datetime.now())

#count = 1
    

# values[parseInt(Math.random() * data.length)]
    
@app.route('/', methods=['POST','GET'])
def index():  
    #Open JSON FILE
    with open('chalicelib/first-names.json') as f:
        first = json.load(f)
    with open('chalicelib/last-names.json') as f:
        last = json.load(f)

    randValue = randint(0, len(first))
    randValue2 = randint(0, len(last))
    reply = '{"fulfillmentMessages": [{"text": {"text": ["My name is ' + first[randValue] + " " +last[randValue2] + '"] } } ]}'
    return reply 


@app.route('/place', methods=['POST','GET'])
def index():
    count = 0
    if app.current_request.query_params is not None:
        filter=app.current_request.query_params
        count=int(filter.get('count'))
    
    #Open JSON FILE
    with open('./chalicelib/places.json') as f:
        data = json.load(f)
    randValue = randint(0, len(data))
    reply = '[{ "location" : "' + data[randValue]  + '" } ' 
    reply = '{"fulfillmentMessages": [{"text": {"text": ["Welcome to ' + data[randValue] + '"] } } ]}'
    return reply

@app.route('/name', methods=['POST','GET'])
def index():  
    #Open JSON FILE
    with open('chalicelib/first-names.json') as f:
        first = json.load(f)
    with open('chalicelib/last-names.json') as f:
        last = json.load(f)

    randValue = randint(0, len(first))
    randValue2 = randint(0, len(last))
    reply = '{"fulfillmentMessages": [{"text": {"text": ["My name is ' + first[randValue] + " " +last[randValue2] + '"] } } ]}'
    return reply 


@app.route('/number', methods=['POST','GET']) #This route will generate a int between 1-1000
def index():
    count = 0
    minValue =  1
    maxValue = 1000
    randValue = randint(minValue, maxValue)
    reply = '{"fulfillmentMessages": [{"text": {"text": ["There are ' + str(randValue) +  '"] } } ]}'
    return reply 

@app.route('/price', methods=['POST','GET'])
def index():
    count = 0
    minValue =  1
    maxValue = 1000
    randValue = "{:.2f}".format(random.uniform(minValue, maxValue))
    reply = '{"fulfillmentMessages": [{"text": {"text": ["The price is $' + randValue +  '"] } } ]}'
    return reply    

