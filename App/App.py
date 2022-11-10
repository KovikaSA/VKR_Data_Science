import numpy as np
import tensorflow as tf
from tensorflow import keras
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

def set_params(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12):

    model = keras.models.load_model("C:/Users/Xyligan/Desktop/VKR/App/keras/")
    prediction = model.predict([param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12])

    return prediction[0][0]

@app.route('/', methods=['post', 'get'])

def app_calculation():
    param_lst = []
    message = ''
    if request.method == 'POST':
        
       # получим данные из наших форм и кладем их в список, который затем передадим функции set_params
        for i in range(1,13,1):
            param = request.form.get(f'param{i}')
            param_lst.append(float(param))
            
        message = set_params(*param_lst)

    # указываем шаблон и прототип сайта для вывода    
    return render_template("index.html", message=message) 

# Запускаем приложение  
app.run(debug=True)