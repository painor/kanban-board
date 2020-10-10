import json
import random
import traceback


def create_new_task(event, context):
    try:

        received_json = json.loads(event["body"])
        task_title = received_json["task_title"]
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
