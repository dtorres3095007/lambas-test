import json
from db.database import Database
from utils import create_response
from jsonschema import validate, ValidationError

with open("schemas/post_user.json", "r") as f:
    user_schema = json.load(f)


def lambda_handler(event, context):
    response = create_response(200, {"message": "User created successfully"})
    try:
        data = json.loads(event.get("body"))
        validate(instance=data, schema=user_schema)
        db = Database()
        db.post_user(data)
    except ValidationError as ve:
        response = create_response(400, {"message": f"Invalid data: {ve.message}"})
    except Exception as e:
        response = create_response(500, {"message": f"Error creating user: {str(e)}"})

    return response
