create_users = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ]
}

login_users = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "token": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "token"
    ]
}

register_successful = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "token": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "id",
        "token"
    ]
}

put_users = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "name",
        "job",
        "updatedAt"
    ]
}
