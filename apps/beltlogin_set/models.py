from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*$')

# apps.secret_key = "keepitasecretbozo"
# hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
# print (hash1)
# $2b$12$Wdc2qwiP6u0WdQdKwmer7.DMIcY6q76GxvrJgaodnpRDmpP8mwkDa
# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = []
        if len(post_data['name']) < 2:
            errors.append("name should be at least 2 characters")
        if len(post_data['alias']) < 2:
            errors.append("alias should be at least 2 characters")
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("email already in use")
        if len(post_data['dob']) != 10:
            errors.append("DOB format is yyyy-mm-dd")
        if len(post_data['dob']) == "":
            errors.append("DOB format is yyyy-mm-dd")
        if not re.match(NAME_REGEX, post_data['name']): # or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        if post_data['password'] != post_data['passconf']:
            errors.append("passwords do not match")

        print ("***********  errors", errors)
        if not errors:
            hash1 = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            password = hash1
            print (hash1)
            new_register = self.create(
                name=post_data['name'],
                alias=post_data['alias'],
                email=post_data['email'],
                dob=post_data['dob'],
                password=hash1
            )
            # print ("added registerer")
            return new_register
        return errors

    def login_validator(self, post_data):
            errors = []
            # check DB for post_data['email']
            if len(self.filter(email=post_data['email'])) > 0:
                # check this user's password
                user = self.filter(email=post_data['email'])[0]
                # print (user_validator)
                # print (user_validator.password.encode())
                # print (post_data['password'].encode())
                if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                    errors.append('email/password incorrect - 1')
            else:
                    errors.append('email/password incorrect - 2')

            if errors:
                return errors
            return user

    def examdpoke(self,post_data, pokeid, user2):
            poked = User.objects.get(id=pokeid)
            poked.pokenum += 1
            print ('*******pokenum*********', poked.pokenum)
            poked.save()
            user = User.objects.get(id=user2)
            user.poke.add(poked)

            return user

class User(models.Model):
        name = models.CharField(max_length=255)
        alias = models.CharField(max_length=255)
        email = models.CharField(max_length=255)
        password = models.CharField(max_length=255)
        dob = models.DateField()
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)
        poke = models.ManyToManyField('self', related_name="userpoke")
        pokenum = models.IntegerField(default=0)
        objects = UserManager()
        def __str__(self):
           return self.email
