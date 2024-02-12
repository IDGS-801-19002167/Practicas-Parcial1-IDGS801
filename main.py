from flask import Flask, render_template, request

import forms,tolerancia

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

@app.route("/tolerancia", methods=["GET", "POST"])
def calctolerancia():
    calct = tolerancia.toleranciaForm(request.form)
    
    banda1 = ""
    banda2 = ""
    banda3 = ""
    rdo = None
    op1 = 0
    value = 0
    valueOro = 0
    valuePlata = 0
    maxValue = 0
    minValue = 0

    color1 = ""
    color2 = ""
    color3 = ""
    color4 = ""
    
    nmcolor1 = ''
    nmcolor2 = ''
    nmcolor3 = ''
    
    colores = {
        '0': '#000000',
        '1': '#CA9D54',
        '2': '#FF0000',
        '3': '#F78526',
        '4': '#FFF223',
        '5': '#00FF00',
        '6': '#0000FF',
        '7': '#C84BAC',
        '8': '#ADADAD',
        '9': '#FFFFFF'
    }
    
    colores2 = {
        '1': '#000000',
        '10': '#CA9D54',
        '100': '#FF0000',
        '1000': '#F78526',
        '10000': '#FFF223',
        '100000': '#00FF00',
        '1000000': '#0000FF',
        '10000000': '#C84BAC',
        '100000000': '#ADADAD',
        '1000000000': '#FFFFFF'
    }
    
    colores3 = {
        '#000000' : 'Negro',
        '#CA9D54' : 'Cafe',
        '#FF0000' : 'Rojo',
        '#F78526' : 'Naranja',
        '#FFF223' : 'Amarillo',
        '#00FF00' : 'Verde',
        '#0000FF' : 'Azul',
        '#C84BAC' : 'Violeta',
        '#ADADAD' : 'Gris',
        '#FFFFFF' : 'Blanco'
    }
    
    if request.method == "POST":
        banda1 = request.form.get("banda1")
        banda2 = request.form.get("banda2")
        banda3 = request.form.get("banda3")
        rdo = calct.rdo.data
        
        if rdo == "Oro":
            op1 = (int(str(banda1) + str(banda2)))
            value = int(op1 * int(banda3))
            
            valueOro = int(value * 0.5)
            maxValue = int(value + valueOro)
            minValue = int(value - valueOro)
            
            color1 = colores[banda1]
            color2 = colores[banda2]
            color3 = colores2[banda3]
            color4 = "#DFCE00"
            
            nmcolor1 = colores3[color1]
            nmcolor2 = colores3[color2]
            nmcolor3 = colores3[color3]
            print(color1, color2, color3)
        elif rdo == "Plata":
            op1 = (int(str(banda1) + str(banda2)))
            value = int(op1 * int(banda3))
            
            valuePlata = int(value * 0.10)
            maxValue = int(value + valuePlata)
            minValue = int(value - valuePlata)
            
            color1 = colores[banda1]
            color2 = colores[banda2]
            color3 = colores2[banda3]
            color4 = "#C9C9C9"
            nmcolor1 = colores3[color1]
            nmcolor2 = colores3[color2]
            nmcolor3 = colores3[color3]
        
    return render_template("resistencia.html", form = calct, banda1 = banda1, banda2 = banda2, banda3 = banda3, 
                           value = value, maxValue = maxValue, minValue = minValue, color1 = color1, color2 = color2, 
                           color3 = color3, color4 = color4, rdo = rdo, nmcolor1 = nmcolor1, nmcolor2 = nmcolor2, nmcolor3 = nmcolor3)
    
if __name__ == "__main__":
    app.run(debug=True)