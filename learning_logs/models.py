# 18-2: Short Entries
# the __str__() method in the Entry model currently appends an ellipsis
# to every instance of Entry when Django shows it in the admin site or
# the shell. Add an if statement to the __str__() method that adds an
# ellipsis only if the entry is longer than 50 characters. Use the admin
# site to add an entry that's fewer than 50 characters in length, and check
# that it doesn't have an ellipsis when viewed.

# 18-3: The Django API
# When you write code to access the data in your project, you're writing a
# query. Skim through the documentation for querying your data at 
# https://docs.djangoproject.com/en/2.2/topics/db/queries/. Much of what
# you see will look new to you, but it will be very useful as you start to
# work on your own projects.

from django.db import models

class Topic(models.Model):
    """ A topic the user is learning about. """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a string representation of the model. """
        return self.text

class Entry(models.Model):
    """ Something specific learned about a topic. """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """ Return a string representation of the model. """
        # 18-2
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."