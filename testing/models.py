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
class Technology( models.Model ):
    name = models.CharField( max_length = 50 )

    def __unicode__( self ):
        return self.name

# Test in area
#
#
class Aspect( models.Model ):
    technology = models.ForeignKey( Technology )
    name = models.CharField( max_length = 200 )

    def __unicode__( self ):
        return self.name

# Test's part (f.e.: language syntax, algorythms)
#
#
class Part( models.Model ):
    aspect     = models.ForeignKey( Aspect )
    name     = models.CharField( max_length = 50 )
    quantity = models.PositiveSmallIntegerField()
    weight   = models.SmallIntegerField()

    def technology( self ):
        if self.aspect:
            return self.aspect.technology
        else:
            return None

    def __unicode__( self ):
        return self.name

# Question in test's part
#
#
class Question( models.Model ):
    part     = models.ForeignKey( Part )
    content  = models.TextField()
    weight   = models.SmallIntegerField( default = 0 )

    def __unicode__( self ):
        return self.content

#
#
#
class Choice( models.Model ):
    question = models.ForeignKey( Question )
    content  = models.CharField( max_length = 200 )
    weight   = models.SmallIntegerField( default = 0 )

    def __unicode__( self ):
        return self.content
