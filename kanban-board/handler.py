import json
import random
import traceback

from base import Task, Session


def create_new_task(event, context):
    try:
        received_json = json.loads(event["body"])
        task_title = received_json["task_title"]
        new_task = Task(task_title)
        session = Session()
        session.add(new_task)
        session.flush()
        session.refresh(new_task)
        body = {
            "message": "Task created successfully",
            "task": {
                "title": task_title,
                "id": new_task.id,
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
