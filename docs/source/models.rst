Models
======

As mentioned in `models <../../../uapi/models.py>`_, any models or classes that are needed such as
data structures or data classes will be structured and laid out using the
`dataclasses` library, which is, conveniently native to the Python standard
library.

.. py:class:: User

   This is a data class representing a User object.

   It is annotated with type hints and follows the data class pattern.

   :param name: Username is an alphanumeric value
   :type name: str
   :param posts: Number of definitions created
   :type posts: int
   :param kwargs: Additional keyword arguments
   :type kwargs: dict

   ``User`` can be instantiated and accessed as shown::

      user = User("John Smith", 2);
      >>>

      print(user.name)
      >>> "John Smith"

      print(user.posts)
      >>> 2

   ``User`` also supports keyword arguments::

      user = User("John Doe", 6, email="johndoe@domain.com")

   ``email`` is now a string declared as an instance variable::

      print(user.email)
      >>> "johndoe@domain.com"

   Instance variables are `immutable`::

      user = User("James Smith", 4)

      user.name = "James"  # Raises a dataclasses.FrozenInstanceError

