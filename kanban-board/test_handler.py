import unittest
import json
from datetime import datetime
from unittest.mock import patch

from base import Task
from handler import create_new_task, start_task
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
                'title': task_title,
                'id': 1,
                'status': 0
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
            task.status = 1
            task.start_date = date
            return task

        with patch('handler.start_new_task', new=return_moch_task):
            res = start_task(received_json, None)
        self.assertEqual(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

        excepted_result = {
            'success': True,
            'message': 'Task started successfully',
            'task': {'id': 1, 'title': 'random_name', 'status': 1, 'start_date': date}
        }
        body = json.loads(res['body'])
        print(body)
        print(excepted_result)
        self.assertTrue(json.dumps(body) == json.dumps(excepted_result))


if __name__ == '__main__':
    unittest.main()
