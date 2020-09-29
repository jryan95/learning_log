"""
19-3: Refactoring

There are two places in views.py where we make sure the user associated
with a topic matches the currently logged in user. Put the code for this
in a function called check_topic_owner(), and call this function where
appropriate.

19-4: Protecting new_entry
Currently, a user can add a new entry to another user's learning log
by entering a URL with the ID of a topic belonging to another user.
Prevent this attack by checking that the current user owns the entry's 
topic before saving the new entry.

19-5: Protected Blog
In your Blog project, make sure each blog post is connected to a particular
user. Make sure all posts are publicly accessible but only registered
users can add posts and edit existing posts. In the view that allows
users to edit their posts, make sure the user is editing their own 
post before processing the form.
"""