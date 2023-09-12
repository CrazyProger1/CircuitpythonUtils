from utils.schemas import Schema, Field


class Role(Schema):
    name = Field(str)


class User(Schema):
    username = Field(str)
    password = Field(str)
    age = Field(int)
    email = Field(str, nullable=True)

    role = Field(Role)


user = User.model_validate({
    'username': 'testuser',
    'password': 'simplepassword',
    'age': 18,
    'email': 'admin@example.com',
    'role': {
        'name': 'admin'
    }
})
print(user)  # User<username=testuser password=simplepassword age=18 email=admin@example.com role=Role<name=admin>>

print(user.model_dump())
# {
# 'username': 'testuser',
# 'password': 'simplepassword',
# 'age': 18,
# 'email': 'admin@example.com',
# 'role': {'name': 'admin'}
# }


user = User.model_validate({
    'username': 'testuser',
    'password': 'simplepassword',
    'age': '18',
    'email': 'admin@example.com',
    'role': {
        'name': 'admin'
    }
})

# utils.exceptions.ValidationError: Field age of schema User must be type of <class 'int'>, not <class 'str'>
