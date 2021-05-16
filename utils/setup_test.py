from django.test import TestCase
from authentication.models import User
from faker import Faker


class TestSetup(TestCase):

    #function that runs first then the test runs
    def setUp(self):

        # print('Test started')

        # self.user = {
        # "username": "username",
        # "email": "email@hmail.com",
        # "password": "password",
        # "password2": "password"
        # }


        self.faker = Faker()
        self.password = self.faker.paragraph(nb_sentences=5)

        self.user = {
            "username": self.faker.name().split(" ")[0],
            "email": self.faker.email(),
            "password": self.password,
            "password2": self.password
        }

    def create_test_user(self):
        user = User.objects.create_user(
            username='username', email='email@app.com')
        user.set_password('password12!')
        user.is_email_verified = True
        user.save()
        return user

    def create_test_user_two(self):
        user = User.objects.create_user(
            username='username2', email='email2@app.com')
        user.set_password('password12!')
        user.save()
        return user

    # fxn that runs after the test has ran
    def tearDown(self):
        # print('Test finished')
        return super().tearDown()


# install coverage (pip install coverage) so that we can know all that part of our code that have been tested
# so that we wan know which one is not tested
# then run - coverage run manage.py test, will do the same test
# then run - coverage run manage.py test -v 2, you see fxn with ok
# for more report
# then run - coverage run manage.py test -v 2 && coverage report
# to specify where
# run - coverage run --source "authentication" manage.py test -v 2 && coverage report
# to test 2 models
# run - coverage run --source "authentication,todo" manage.py test -v 2 && coverage report
# can create a .coveragerc file and specify the files you want to omit
#then can run back - coverage run manage.py test -v 2 && coverage report
# to see files not tested, you can generate a html file by using the command below
# run - coverage run manage.py test -v 2 && coverage report && coverage html
# after running the above it will create a folder called htmlcov, make sure to add htmlcov to .gitignore
# can also get the data in xml file by running - coverage run manage.py test -v 2 && coverage report && coverage xml
# add coverage.xml file to .gitignore file too

