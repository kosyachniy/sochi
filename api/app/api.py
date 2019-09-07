from flask import request, jsonify
from app import app

from mongodb import db


@app.route('/get', methods=['POST'])
def get():
	print(request.json)

	# Получение данных

	db_filter = {
		'_id': False,
	}

	apartments = []

	for apartment in db['apartments'].find({}, db_filter):
		apartment['user'] = db['users'].find_one({'id': apartment['user']}, db_filter)
		apartments.append(apartment)

	# Ответ

	res = {
		'appartments': apartments,
	}

	return jsonify(res)