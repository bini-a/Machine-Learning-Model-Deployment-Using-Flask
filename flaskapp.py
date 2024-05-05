#These lines import necessary modules and functions
from flask import Flask, render_template, request
import pickle

#we initialize the flask
#This line creates a Flask application object which will be used to handle requests and responses
app = Flask(__name__)

# load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
#Define a function will return the index of the current home page that we want to load
def home():
    result = ''
    return render_template('index.html', **locals())

#This line is a decorator that defines a route for the root URL ‘/’. The route handles both GET and POST requests.
#GET requests are used for retrieving data, while POST requests are used for submitting data to be processed.
@app.route('/predict', methods=['POST', 'GET'])
#we define another function to predict the data
#This function will request the user data from the webpage and predict the label from the loaded model and return to the webpage
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    return render_template('index.html', **locals()) #Renders the index.html template, passing the variable to it, which can then be displayed to the user.
#Alternatively, you can define the predict function without explicitly mentioning each feature
#def predict():
    #float_features = [float(x) for x in request.form.values()]
    #features = [np.array(float_features)]
    #prediction = model.predict(features)
    #return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))

#This block of code runs the Flask application when the script is executed directly (__name__ == ‘__main__’). 
#The debug=True argument enables debug mode, which provides helpful error messages in the browser during development.
#If the debug argument is set to False when running the Flask application, debug mode will be disabled.
if __name__ == '__main__':
    app.run(debug=True)
