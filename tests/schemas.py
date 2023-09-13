import unittest
from utils import schemas


class Role(schemas.Schema):
    name = schemas.Field(str)


class User(schemas.Schema):
    username = schemas.Field(str)
    password = schemas.Field(str)
    age = schemas.Field(int)
    email = schemas.Field(str, nullable=True)

    role = schemas.Field(Role)
    test: int
    test2: int = 10


data = {
    'username': 'testuser',
    'password': 'simplepassword',
    'age': 18,
    'email': 'admin@example.com',
    'role': {
        'name': 'admin'
    },
    'test': 1,
    'test2': 5
}


class TestSchemas(unittest.TestCase):
    def test_dump_validate(self):
        user = User.model_validate(data)
        self.assertEqual(data, user.model_dump())


if __name__ == '__main__':
    unittest.main()
