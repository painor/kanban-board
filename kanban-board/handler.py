import json
import random
import traceback

from base import add_new_task


def create_new_task(event, context):
    try:
        received_json = json.loads(event["body"])
        task_title = received_json["task_title"]
        task_id = add_new_task(task_title)
        body = {
            "message": "Task created successfully",
            "task": {
                "title": task_title,
                "id": task_id,
                "status": 0
            }
        }
        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }


def resolve_task(event, context):
    try:
        received_json = json.loads(event["body"])
        task_title = received_json["task_id"]
        task_id = random.randint(1, 100)

        body = {
            "message": "Task created successfully",
            "task": {
                "title": task_title,
                "id": task_id
            }
        }
        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
