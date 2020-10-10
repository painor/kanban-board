import unittest
import json
from datetime import datetime
from unittest.mock import patch

from base import Task, Status, get_all_tasks
from handler import create_new_task, start_task, resolve_task, get_tasks, get_task
from string import ascii_lowercase
import random


class TestHandler(unittest.TestCase):
    """ Tests handler methods """

    def test_create_new_task(self):
        """ Tests create_new_task """
        task_title = ''.join(random.choice(ascii_lowercase) for _ in range(8))

        received_json = {'body': json.dumps({
            'task_title': task_title
        })}
        # monkey patch database call
        with patch('handler.add_new_task', new=lambda x: 1):
            res = create_new_task(received_json, None)

        self.assertEqual(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

        excepted_result = {
            'success': True,
            'message': 'Task created successfully',
            'task': {
                'id': 1,
                'title': task_title,
                'status': Status.NEW
            }
        }
        body = json.loads(res['body'])
        self.assertTrue(json.dumps(body) == json.dumps(excepted_result))

    def test_start_task(self):
        """ Tests start_task """
        task_id = 1
        received_json = {'body': json.dumps({
            'task_id': task_id
        })}

        # monkey patch database call
        date = datetime.now().timestamp()

        def return_moch_task(*args):
            task = Task('random_name')
            task.id = 1
            task.status = Status.IN_PROGRESS
            task.start_date = date
            return task

        with patch('handler.start_new_task', new=return_moch_task):
            res = start_task(received_json, None)
        self.assertEqual(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

        excepted_result = {
            'success': True,
            'message': 'Task started successfully',
            'task': {'id': 1, 'title': 'random_name', 'status': Status.IN_PROGRESS, 'start_date': date}
        }
        body = json.loads(res['body'])
        self.assertTrue(json.dumps(body) == json.dumps(excepted_result))

    def test_resolve_task(self):
        """Tests resolve_task"""
        task_id = 1
        received_json = {'body': json.dumps({
            'task_id': task_id
        })}
        # monkey patch database call
        date = datetime.now().timestamp()

        def return_mock_task(*args):
            task = Task('random_name')
            task.id = 1
            task.status = Status.DONE
            task.start_date = date
            task.end_date = date + 3600
            task.price = 10.0
            return task

        with patch('handler.resolve_a_task', new=return_mock_task):
            res = resolve_task(received_json, None)
        self.assertEqual(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

        excepted_result = {'success': True, 'message': 'Task started successfully',
                           'task': {'id': 1, 'title': 'random_name', 'status': 2, 'start_date': date,
                                    'price': 10.0}}

        body = json.loads(res['body'])
        self.assertTrue(json.dumps(body) == json.dumps(excepted_result))

    def test_get_tasks(self):
        """Tests get_tasks"""

        # monkey patch database call
        date = datetime.now().timestamp()

        def return_moch_task(*args):
            tasks = []
            task1 = Task('random_name')
            task1.id = 1
            task1.status = Status.DONE
            task1.start_date = date
            task1.end_date = date + 3600
            task1.price = 10.0
            tasks.append(task1)
            task2 = Task('random_name')
            task2.id = 2
            task2.status = Status.DONE
            task2.start_date = date
            task2.end_date = date + 3600
            task2.price = 10.0
            tasks.append(task2)
            return tasks

        with patch('handler.get_all_tasks', new=return_moch_task):
            res = get_tasks({"queryStringParameters": None}, None)
        self.assertEqual(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

        excepted_result = {'success': True, 'tasks': [
            {'id': 1, 'title': 'random_name', 'status': 2, 'start_date': date,
             'end_date': date+3600, 'price': 10.0},
            {'id': 2, 'title': 'random_name', 'status': 2, 'start_date': date,
             'end_date': date+3600, 'price': 10.0}], 'total': 2}

        body = json.loads(res['body'])


        self.assertTrue(json.dumps(body) == json.dumps(excepted_result))

    def test_get_task(self):
        """Tests get_task"""

        # monkey patch database call
        date = datetime.now().timestamp()

        def return_moch_task(*args):
            task = Task('random_name')
            task.id = 1
            task.status = Status.DONE
            task.start_date = date
            task.end_date = date + 3600
            task.price = 10.0
            return task

        with patch('handler.get_a_task', new=return_moch_task):
            res = get_task({"pathParameters": {"id": "1"}}, None)
        self.assertEqual(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

        excepted_result = {'success': True,
                           'task': {'id': 1, 'title': 'random_name', 'status': 2, 'start_date': date,
                                    'end_date': date + 3600, 'price': 10.0}}

        body = json.loads(res['body'])
        self.assertTrue(json.dumps(body) == json.dumps(excepted_result))


if __name__ == '__main__':
    unittest.main()
