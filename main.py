# importing the lib
from flask import Flask , render_template, request
import joblib

app = Flask(__name__)

#load the model
model = joblib.load('model/diabetic_80.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['post']) # decorator
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if result[0]==1:
        data = 'person is diabatic'
    else:
        data = 'person is not diabatic'

      
    return render_template('predict.html',data=data)

app.run(debug = True) # should be always at the end