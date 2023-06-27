import numpy as np
import os
from flask import Flask, request, render_template
from keras.models import load_model
from keras.utils import load_img,img_to_array
from keras.applications.xception import preprocess_input

model=load_model(r"OneDrive\Desktop\Naan Mudhalvan\Project\ibm_flask\ibm_mushroom.h5")

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/input')
def input1():
    return render_template("input.html")
    

@app.route('/predict', methods=["GET","POST"])
def res():
    if request.method=="POST":
        f=request.files['image']
        basepath=os.path.dirname(__file__)
        filepath=os.path.join(basepath,'uploads',f.filename)
        f.save(filepath)
        
        img=load_img(filepath,target_size=(224,224,3))
        x=img_to_array(img)
        x=np.expand_dims(x,axis=0)
        
        img_data=preprocess_input(x)
        prediction=np.argmax(model.predict(img_data), axis=1)
        
        index=['Boletus','Lactarius','Russula']
        
        result=str(index[prediction[0]])
        print(result)
        return render_template('output.html', prediction=result)
if __name__ == "__main__":
    app.run(debug=False)