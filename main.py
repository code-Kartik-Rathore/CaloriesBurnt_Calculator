from flask import Flask, request, url_for, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')

def home_page():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])

def predict():
   
        int_features = []
   
        # Convert relevant form values to integers or floats
        int_features.append(int(request.form['userid']))  # Assuming UserId is an integer
        # You may need to handle Gender differently based on your model's requirements
        gender = request.form['Gender']
        if gender == 'male':
             int_features.append(1)
        else:
            int_features.append(0)
        
        int_features.append(int(request.form['Age']))
        int_features.append(float(request.form['Height']))
        int_features.append(float(request.form['Weight']))
        int_features.append(int(request.form['Duration']))
        int_features.append(int(request.form['Heart_Rate']))
        int_features.append(float(request.form['Body_Temp']))
        
        
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = np.round(prediction[0], 2)

        return render_template('index.html', prediction_text='calories burnt will be {}'.format(output))


if __name__ == '__main__':
    app.run(debug = True)