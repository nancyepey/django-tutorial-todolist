from utils.setup_test import TestSetup
from django.test import TestCase
from authentication.models import User
from todo.models import Todo


# class TestModel(TestCase):

#     def test_should_create_todo(self):

#         user = User.objects.create_user(username='username', email='email@app.com')
#         user.set_password('password12!')
#         user.save()

#         todo = Todo(owner=user, title="Buy milk", description='get it done')

#         todo.save()

#         #str representation of the todo
#         self.assertEqual(str(todo), 'Buy milk')



class TestModel(TestSetup):

    def test_should_create_user(self):
        user = self.create_test_user()
        todo = Todo(owner=user, title="Buy milk", description='get it done')
        todo.save()
