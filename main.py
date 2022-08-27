from flask import Flask
from flask import request
import joblib

app = Flask(__name__)
@app.route('/')
def home():
  return render_template('home.html')


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
  if request.method == "POST":

    os = request.form.get('Operating System')
    country = request.form.get('Country')
    device = request.form.get('isMobile')
    page_views = request.form.get('Page Views')
    try:
      prediction = predictTransaction(os, country, device, page_views)
      return render_template('predict.html', prediction=prediction)
    except ValueError:
      return "Please Enter valid values"
    pass
  pass


def predictTransaction(os, country, device, page_views):
  data = [os, country, device, page_views]
  print(data)
  data = np.array(data).astype(np.float64)
  data = data.reshape(1, -1)
  print(data)
  file = open("transaction_model.pkl", 'rb')
  trained_model = joblib.load(file)
  prediction = trained_model.predict(data)
  return prediction

  pass


if __name__ == '__main__':
  app.run(debug=True)
