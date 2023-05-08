import requests
import json
from flask import Flask, render_template, request,redirect, url_for,make_response


from deep_translator import GoogleTranslator


app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    cantidad = ''
    grado = ''
    coeficiente = ''
    tiempo = ''
    lista_cantidad =''
    if request.method == 'POST':
        grado = int(request.form['grado'])
        coeficiente = int(request.form['coeficiente'])
        tiempo = int(request.form['tiempo'])
        print(grado)
        print(coeficiente)
        print(tiempo)
        if grado and coeficiente and tiempo:
            cantidad = access_to_api(grado,coeficiente,tiempo)
            lista_cantidad = []
            for elem in cantidad:
                lista_cantidad += elem.split('\n')
            # return redirect(url_for('index', cantidad=cantidad[0]))
    
    # cantidad = request.args.get('cantidad')
    print(lista_cantidad)
    return render_template('index.html', cantidad=cantidad,lista_cantidad=lista_cantidad)

def access_to_api(grado,coeficiente,tiempo):
    print("hola mmgvs")
    api_key = ''
    query =  'second derivative of 3x^2 + 2x + 1'
    url = f'http://api.wolframalpha.com/v2/query?appid={api_key}&input={query}&output=json&podstate=Step-by-step%20solution&traslation=true'
    response = requests.get(url)
    response_json = json.loads(response.text)
    print(response_json)
    steps = ''
    steps_ES = ''
    steps_ES_IMG = None
    if response_json:
        for r in response_json['queryresult']['pods'][0]['subpods']:
            steps+=r['plaintext'] + "\n"
        img= response_json['queryresult']['pods'][0]['subpods'][1]['img']['src']
        steps=steps.replace('|', '')
        steps_ES = GoogleTranslator(source='auto', target='es').translate(steps) 
        steps_ES_IMG = GoogleTranslator(source='auto', target='es').translate(img) 
        print("steps")
        print(steps)
        print("stepses")
        print(steps_ES)

    return(steps_ES,steps_ES_IMG)
 

if __name__ == '__main__':
    app.run(debug=True)
