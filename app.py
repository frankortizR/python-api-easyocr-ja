
from distutils.log import debug
from flask import Flask, request
import cv2
import easyocr

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./Archivos"

@app.route('/')
def home():
    return 'This is home'

@app.route('/hi')
def sayhi():
    return 'Hi madafaka'

@app.route('/subirfoto', methods = ['POST'])
def Aiforcharacter():
    if request.method == 'POST':
        theimage = request.files['archivo'] #lleva el nombre de la etiqueta name en el input html
        theimage.save('./static/' +'imagefortest.jpg')

        reader = easyocr.Reader(["ja"], gpu=False)
        image1 = cv2.imread("./static/imagefortest.jpg")

        result = reader.readtext(image1)
        for res in result:
            print("resultado", res)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if res[2]>0.6:
            return "Reconocio el caracter"
            #return str(result[1])
        return "archivo subido con exito"
    else:
        return "no POST method"

if __name__ == '__main__':
    app.run(debug = True, port=4000)