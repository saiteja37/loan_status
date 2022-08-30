from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np
model=pickle.load(open("teja.pkl","rb"))
df=pd.read_csv("teja.csv")
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def ind():
    edu=df["Education"].unique()
    df["Self_Employed"]=df["Self_Employed"]
    emps=df["Self_Employed"].unique()
    prop=df['Property_Area'].unique()
    df['Credit_History']=df['Credit_History']
    cred = df['Credit_History'].unique()
    loan= request.form.get('loan')
    income=request.form.get("income")
    ed=request.form.get("company")
    emp=request.form.get("emp")
    pro=request.form.get("pro")
    cre=request.form.get("cre")
    pred = model.predict(pd.DataFrame([[ed, emp, income, loan, cre, pro]],columns=['Education', 'Self_Employed', 'ApplicantIncome', 'LoanAmount','Credit_History', 'Property_Area']))
    if pred == "N":
        data = "Rejected"
    else:
        data = "Accepted"
    return render_template("index.html",edu=edu,emps=emps,prop=prop,cred=cred,data=data)


















if __name__ == '__main__':
    app.run(debug=True)