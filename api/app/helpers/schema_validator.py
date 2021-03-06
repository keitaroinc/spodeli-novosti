# -*- coding:utf-8 -*-
from jsonschema import Draft4Validator, FormatChecker


def validate_subscriber(subscriber):
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string",
                      "format": "email"},
        },
        "required": ["name", "email"],
    }

    validator = Draft4Validator(subscriber, format_checker=FormatChecker())

    return validator.validate(subscriber, schema)


def validate_newsletter(subscriber):
    schema = {
        "type": "object",
        "properties": {
            "subject": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["subject", "body"],
    }

    validator = Draft4Validator(subscriber)

    return validator.validate(subscriber, schema)
