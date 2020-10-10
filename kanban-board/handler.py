import json
import random
import traceback

from base import add_new_task, start_new_task


def create_new_task(event, context):
    try:
        received_json = json.loads(event["body"])
        task_title = received_json["task_title"]
        task_id = add_new_task(task_title)
        body = {
            "success": True,
            "message": "Task created successfully",
            "task": {
                "id": task_id,
                "title": task_title,
                "status": 0
            }
        }
        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except Exception as e:
        traceback.print_exc()
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }


def start_task(event, context):
    try:
        received_json = json.loads(event["body"])
        task_id = received_json["task_id"]
        task = start_new_task(task_id)
        body = {
            "success": True,
            "message": "Task started successfully",
            "task": {
                "id": task.id,
                "title": task.title,
                "status": task.status,
                "start_date": task.start_date
            }
        }
        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except Exception as e:
        traceback.print_exc()
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
