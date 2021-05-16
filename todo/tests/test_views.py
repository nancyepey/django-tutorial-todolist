from utils.setup_test import TestSetup
from authentication.models import User
from todo.models import Todo
from django.urls import reverse


class TestModel(TestSetup):

    def test_should_create_atodo(self):

        # create user
        user = self.create_test_user()
        #login user
        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })

        # get todos
        todos = Todo.objects.all()

        # the should be 0 todo for the new login user
        self.assertEqual(todos.count(), 0)

        #creating a todo for the login user
        response = self.client.post(reverse('create-todo'), {
            'owner': user,
            'title': "Hello do this",
            'description': "Remember to do this"
        })

        #saving the todo ie adding the todo in todos
        updated_todos = Todo.objects.all()

        #checking if the todo has increase ie there's one todo now after adding it
        self.assertEqual(updated_todos.count(), 1)

        #checking the status
        self.assertEqual(response.status_code, 302)
        # note when you write an assertEqual in a test make sure to write more than one assertions
        # to assert more than one scenario
        # many scenarios can happen in the process of doing something