.. module:: models
   :synopsis: Container for common data structures used to represent data.

Models
******

As mentioned in `models <../../../uapi/models.py>`_, any models or classes that are needed such as
data structures or data classes will be structured and laid out using the
`dataclasses` library, which is, conveniently native to the Python standard
library.

----

.. autoclass:: User

``User`` can be instantiated and accessed as shown::

  user = User("John Smith", 2);
  print(user.name)
  print(user.posts)

Output::

  >>> "John Smith"
  >>> 2

``User`` also supports keyword arguments::

  user = User("John Doe", 6, email="johndoe@domain.com") # Email is now an instance variable
  print(user.email)

Output::

  >>> "johndoe@domain.com"

Variables are immutable by default::

  user = User("James Smith", 4)

Output::

  >>> user.name = "James"  # Raises a dataclasses.FrozenInstanceError

