import unittest
import json
from unittest.mock import patch

from handler import create_new_task
from string import ascii_lowercase
import random


class TestHandler(unittest.TestCase):
    """ Tests handler methods """

    def test_create_new_task(self):
        """ Tests create_new_task """
        task_title = ''.join(random.choice(ascii_lowercase) for _ in range(8))

        received_json = {"body": json.dumps({
            "task_title": task_title
        })}
        # monkey patch database call
        with patch('base.add_new_task', new=lambda x: 1):
            res = create_new_task(received_json, None)

        self.assertEqual(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

        excepted_result = {
            "message": "Task created successfully",
            "task": {
                "title": task_title,
                "id": 1,
                "status": 0
            }
        }
        body = json.loads(res['body'])
        self.assertTrue(body['message'] == excepted_result['message'])
        self.assertTrue(body['task']["title"] == excepted_result['task']["title"])


if __name__ == '__main__':
    unittest.main()
