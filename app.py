from flask import Flask, request,jsonify
import json
app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my flask practice app"

@app.route('/cal',methods=["GET","POST"])
def math_operator():
    operation=request.json["operation"]    # we are not requesting from html, we are requesting from postman
    number1=request.json["number1"]
    number2=request.json["number2"]


    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multiply":
        result=int(number1)*int(number2)
    elif operation=="divison":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return jsonify(result)


if __name__=='__main__':
    app.run(debug=True)