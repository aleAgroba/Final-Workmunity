#Importar librerias
import bottle
import requests
import json

#Declaracion de listas
respuesta = []
empresas = []
lugares = []
puestos = []
vacantes = []

#Pagina principal
@bottle.route('/')
def home_page():
    return bottle.template('index.tpl')

#Cargar hoja de estilo
@bottle.route('/home/ale/Escritorio/bottle/style/:filename#.*#')
def send_static(filename):
    return bottle.static_file(filename, root='/home/ale/Escritorio/bottle/style/')

#Metodo donde se toman los datos del formulario
@bottle.route('/respuesta', method='POST')
def respuesta():
    palabraclave = bottle.request.forms.get('palabraclave')
    provincia = bottle.request.forms.get('provincia')
    categoria = bottle.request.forms.get('categoria')
    sector = bottle.request.forms.get('sector')
    estudios = bottle.request.forms.get('estudios')

    respuesta = requests.get("http://api.workmunity.com/1/search_offers?", params={"return":"json",
  "callback":"json_callback","cache":"on","lang":"es","locale":"es","echo":"test","results":"10",
	"keywords":palabraclave,"country":"es","state":provincia,"town":"0","radio":"on","studies":estudios,"level":"0",
	"category":categoria,"subcategory":"0","sector":sector,"salary":"0","contract":"0","workday":"0",
	"only_verified":"off","only_without_experience":"off"})

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
        empresas.append(json.loads(respuesta.text)[i][u'company'])

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
	lugares.append(json.loads(respuesta.text)[i]['town_str'])

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
	puestos.append(json.loads(respuesta.text)[i][u'position'])

    for i in xrange(0,int(len(json.loads(respuesta.text)))):
	vacantes.append(json.loads(respuesta.text)[i][u'vacancies'])

    return bottle.template('respuesta.tpl',ofertas=len(json.loads(respuesta.text)),empresas=empresas,lugares=lugares,puestos=puestos,vacantes=vacantes,palabraclave=palabraclave,provincia=provincia,categoria=categoria,estudios=estudios,sector=sector)
bottle.debug(True)
bottle.run(host='localhost',port=8080)
