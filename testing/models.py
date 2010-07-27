from django.db import models
from django.contrib.auth import User

# Create your models here.

# Additional user information
#
#
class Contact( User ):
  user_id = models.ForeignKey( User )
  jabber  = models.CharField( max_length = 50 )
  # ... more to add


