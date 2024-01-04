import json
from db.database import Database
from utils import create_response


def lambda_handler(event, context):
    response = {}
    try:
        db = Database()
        users = db.get_user()
        resp = [dict(user) for user in users]
        response = create_response(200, {"users": resp})

    except Exception as e:
        response = create_response(500, {"message": f"Error getting user: {str(e)}"})

    return response
