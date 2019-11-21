import json, requests
from flask import make_response
from flask import Flask, request
from flask_cors import CORS
from flask import jsonify
from util import Translate

app = Flask(__name__)
CORS(app)
#headers = {'x-api-key': ''}
message404 = { 'message' : "Erro ao requisitar dados da fonte original"}
message400 = { 'message' : "O parâmetro enviado é inválido"}
fors = []

@app.route("/breeds", methods=['GET'])
def breeds():
    params = {'attach_breed': '', 'page': '', 'limit': ''}
    response = requests.get("https://api.thedogapi.com/v1/breeds", params=params)
    if response.status_code == 404:
        return make_response(message404, response.status_code)
    breeds = json.loads(response.content)
    breedResponse = []

    for breed in breeds:
        temperaments = []
        bredsfor =[]
        if "temperament" in breed:
            tempSplit = breed["temperament"].split(",")
            for temperament in tempSplit:
                temperaments.append(Translate.temperament(temperament.strip()))
            breed["temperament"] = temperaments
        else:
            breed["temperament"] = []

        if "bred_for" in breed:
            bredforSplit = breed["bred_for"].split(",")
            for bredfor in bredforSplit:
                bredsfor.append(Translate.bredfor(bredfor.strip()))
            breed["bred_for"] = bredsfor
        else:
            breed["bred_for"] = []

        breedResponse.append(breed)

    return make_response(jsonify(breedResponse), 200)

@app.route("/breedsbyname", methods=['GET'])
def breedsByName():
    breed_name_param = request.args['breed_name']

    if breed_name_param == '' or breed_name_param is None:
        return make_response(message400, 400)

    params = {'q': breed_name_param }
    response = requests.get("https://api.thedogapi.com/v1/breeds/search", params=params)
    if response.status_code == 404:
        return make_response(message404, response.status_code)
    breeds = json.loads(response.content)
    breedResponse = []

    for breed in breeds:
        temperaments = []
        bredsfor =[]
        if "temperament" in breed:
            tempSplit = breed["temperament"].split(",")
            for temperament in tempSplit:
                temperaments.append(Translate.temperament(temperament.strip()))
            breed["temperament"] = temperaments
        else:
            breed["temperament"] = []

        if "bred_for" in breed:
            bredforSplit = breed["bred_for"].split(",")
            for bredfor in bredforSplit:
                bredsfor.append(Translate.bredfor(bredfor.strip()))
            breed["bred_for"] = bredsfor
        else:
            breed["bred_for"] = []

        breedResponse.append(breed)

    return make_response(jsonify(breeds), 200)

@app.route("/breedimage", methods=['GET'])
def breedImage():
    breed_id = request.args['breed_id']
    if breed_id == '' or breed_id is None:
        return make_response(message400, 400)

    params = {'breed_id': breed_id }
    response = requests.get("https://api.thedogapi.com/v1/images/search", params=params)

    if response.status_code == 404:
        return make_response(message404, response.status_code)
    elif response.status_code == 200:
        breeds = json.loads(response.content)
        image = { "id": breeds[0]["id"], "image": breeds[0]["url"]}
        return make_response(jsonify(image), 200)


if __name__ == "__main__":
    app.run()