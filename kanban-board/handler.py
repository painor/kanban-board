import json
import random
import traceback
from lambda_decorators import cors_headers

from base import add_new_task, start_new_task, resolve_a_task, get_all_tasks, get_a_task


@cors_headers
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


@cors_headers
def start_task(event, context):
    try:
        received_json = json.loads(event["body"])
        task_id = received_json["task_id"]
        task = start_new_task(task_id)
        body = {
            "success": True,
            "message": "Task started successfully",
            "task": task.to_dict()
        }
        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except Exception as e:
        traceback.print_exc()
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }


@cors_headers
def resolve_task(event, context):
    try:
        received_json = json.loads(event["body"])
        task_id = received_json["task_id"]
        task = resolve_a_task(task_id)

        body = {
            "success": True,
            "message": "Task started successfully",
            "task":task.to_dict()
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


@cors_headers
def get_tasks(event, context):
    try:
        filter_by = None
        if event["queryStringParameters"]:
            if "filter" in event["queryStringParameters"]:
                allowed_filters = ("new", "in_progress", "done")
                if event["queryStringParameters"] not in allowed_filters:
                    raise Exception(f"Unknown filter value '{event['queryStringParameters']}'")
                filter_by = allowed_filters.index(event['queryStringParameters'])
        tasks = get_all_tasks(filter_by)
        tasks = [task.to_dict() for task in tasks]
        return {
            "statusCode": 200,
            "body": json.dumps({"success": True,
                                "tasks": tasks,
                                "total": len(tasks)})
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


@cors_headers
def get_task(event, context):
    try:
        param: str = event["pathParameters"]["id"]
        if not param.isdigit():
            raise Exception("ID should be an integer")
        param: int = int(param)
        return {
            "statusCode": 200,
            "body": json.dumps({"success": True,
                                "task": get_a_task(param).to_dict()})
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
