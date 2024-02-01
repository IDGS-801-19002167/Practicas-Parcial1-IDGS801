from flask import Flask, render_template, request

import forms

app = Flask(__name__)

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html") 

@app.route("/resultado",methods=["GET","POST"])
def resul():   
    if request.method == "POST":
        if request.form.get("checksum"):
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return "La suma de {} + {} es = {}".format(num1,num2,str(int(num1)+int(num2)))
        
        if request.form.get("checkrest"):
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return "La resta de {} - {} es = {}".format(num1,num2,str(int(num1)-int(num2)))
        
        if request.form.get("checkmulti"):
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return "La multiplicacion de {} X {} es = {}".format(num1,num2,str(int(num1)*int(num2)))
        
        if request.form.get("checkdiv"):
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return "La division de {} / {} es = {}".format(num1,num2,str(int(num1)//int(num2)))
    

@app.route("/ecuacion", methods=["GET","POST"])
def ecuacion():
    calculo = forms.CalculateForm(request.form)
    
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    resultC = 0
    
    if request.method == "POST":
        number1 = calculo.number1.data
        number2 = calculo.number2.data
        number3 = calculo.number3.data
        number4 = calculo.number4.data
        
        resultC = ((int(number3) - int(number1))**2 + ((int(number4) - int(number2)))**2)**0.5
        
    return render_template("form.html", form = calculo, number1 = number1, number2 = number2, number3 = number3, number4 = number4, resultC = resultC)
    
if __name__ == "__main__":
    app.run(debug=True)