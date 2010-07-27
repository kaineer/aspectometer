from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Additional user information
#
#
#class Contact( User ):
#    user    = models.ForeignKey( User, related_name = id )
#    jabber  = models.CharField( max_length = 50 )
#  # ... more to add

# Knowledge area
#
#
class Area( models.Model ):
    name = models.CharField( max_length = 50 )

    def __unicode__( self ):
        return self.name

# Test in area
#
#
class Test( models.Model ):
    area = models.ForeignKey( Area )
    name = models.CharField( max_length = 200 )

    def __unicode__( self ):
        return self.name

# Test's part (f.e.: language syntax, algorythms)
#
#
class Part( models.Model ):
    test     = models.ForeignKey( Test )
    name     = models.CharField( max_length = 50 )
    quantity = models.PositiveSmallIntegerField()
    weight   = models.SmallIntegerField()

    def __unicode__( self ):
        return self.name

# Question in test's part
#
#
class Question( models.Model ):
    part     = models.ForeignKey( Part )
    content  = models.TextField()

#
#
#
class Choice( models.Model ):
    question = models.ForeignKey( Question )
    weight   = models.SmallIntegerField( default = 0 )
