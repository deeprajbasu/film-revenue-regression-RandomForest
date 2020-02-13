
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
#import pandas as pd

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:


            #  reading the inputs given by the user
            budget=float(request.form['budget'])
            genres = float(request.form['genres'])
            popularity = float(request.form['popularity'])
            production_companies = float(request.form['production_companies'])
            production_countries = float(request.form['production_countries'])
            release_date = float(request.form['release_date'])
            runtime = float(request.form['runtime'])
            spoken_languages = float(request.form['spoken_languages'])
            vote_average = float(request.form['vote_average'])
            vote_count = float(request.form['vote_count'])

            # Loading the saved models into memory
            filename_scaler = 'scaler_model.pickle'
            filename = 'RandomForest_model.pickle'


            scaler_model = pickle.load(open(filename_scaler, 'rb'))
            loaded_model = pickle.load(open(filename, 'rb'))

            # predictions using the loaded model file
            scaled_data = scaler_model.transform([[budget, genres,
                                                   popularity, production_companies, production_countries,
                                                   release_date, runtime, spoken_languages,vote_average,vote_count]])
            prediction = loaded_model.predict(scaled_data)
            print('prediction is', prediction[0])
            # if prediction[0] == 1:
            #     result = 'The Patient is Diabetic'
            # else:
            #     result = 'The Patient is not Diabetic'




            print('prediction is', prediction[0])
            # showing the prediction results in a UI



            return render_template('results.html',prediction=prediction[0])


        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app