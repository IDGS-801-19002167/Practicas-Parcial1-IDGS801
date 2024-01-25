from flask import Flask,render_template,request

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
    
    
if __name__ == "__main__":
    app.run(debug=True)