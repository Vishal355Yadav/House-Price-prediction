# from crypt import methods
from operator import methodcaller
import pickle
from winreg import REG_WHOLE_HIVE_VOLATILE
from flask import Flask,render_template,request
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    area=int(request.form.get('area1'))
    bedrooms=int(request.form.get('bedroom'))
    bathrooms=int(request.form.get('bathroom'))
    stories=int(request.form.get('stories'))
    mainroad=int(request.form.get('mainroad'))
    guestroom=int(request.form.get('guestroom'))
    basement=int(request.form.get('basement'))
    hotwaterheating=int(request.form.get('hotwater'))
    airconditioning	=int(request.form.get('aircondition'))
    parking	=int(request.form.get('parking'))
    prefarea=0
    furnished=0
    semi_furnished=0	
    unfurnished=0
    if request.form['furnish']=="furnished":
        furnished=1
    elif request.form['furnish']=="unfurnished":
        unfurnished=1 
    else:
        semi_furnished=1
       

    li=[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnished,semi_furnished,unfurnished]
    price=model.predict([li])
    output=round(price[0],2)
    return render_template('index.html',predict_text=f'Price of house is {output}/-')



if __name__=='__main__':
    app.run(debug=True)    
