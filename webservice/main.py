from flask import Blueprint, Flask, request

from .extensions import mongo

main = Blueprint('main', __name__)

#.\.venv\Scripts\activate.bat to activate virtual env on windows
#flask run to start the server

@main.route('/api/v1/payment', methods=['POST'])
def record_payment():
    query_parameters = request.json

    payment_email = query_parameters.get('m_email')
    payment_username = query_parameters.get('m_username')
    payment_name = query_parameters.get('m_designation')
    payment_date = query_parameters.get('m_date')
    payment_montant = query_parameters.get('m_montant')
    payment_mode = query_parameters.get('m_mode')

    paiements_collection = mongo.db.paiements
    try:
        paiements_collection.insert_one({"nom": payment_username,
                                    "email": payment_email,
                                    "designation":payment_name,
                                    "date":payment_date, 
                                    "montant":payment_montant, 
                                    "mode":payment_mode})
    except mongo.errors.WriteError as e :
        return "Erreur dans l'ajout du paiement : %s" % e, 400
    
    return "Paiement enregistré !", 201

@main.route('/api/v1/payment', methods=['GET'])
def get_user_last_payment():
    return "oui"