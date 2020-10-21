import json

from django.test import (
    TestCase,
    Client
)

client = Client()

class SignupTest(TestCase):
    def test_signup_post_success(self):
        data = {
            'name'         : '조윤민',
            'birthdate'    : '2001-09-23',
            'identifier'   : 'hj1234',
            'password'     : '1q2w3e4r!',
            'gender'       : '여자',
            'phone_number' : '01012345258',
            'email'        : 'qwer@qwer.com'
        }

        response = client.post('/user/signup', json.dumps(data), content_type = 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "message" : "SUCCESS"
        })