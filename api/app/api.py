from flask import request, jsonify
from app import app

from mongodb import db


@app.route('/get', methods=['POST'])
def get():
	x = request.json
	lat, lng = x['lat'], x['lng']
	r = x['radius'] if 'radius' in x else 0

	# Получение данных

	db_filter = {
		'_id': False,
	}

	apartments = []

	for apartment in db['apartments'].find({}, db_filter):
		if not r or ((lat - apartment['location'][0]) ** 2 + (lng - apartment['location'][1]) ** 2) ** 0.5 <= r:
			apartment['user'] = db['users'].find_one({'id': apartment['user']}, db_filter)
			apartments.append(apartment)

	# Ответ

	res = {
		'appartments': apartments,
	}

	return jsonify(res)