from aspectometer.testing.models import Area, Test, Part, Question
from django.contrib import admin


class PartInline( admin.TabularInline ):
    model = Part
    extra = 3

class TestAdmin( admin.ModelAdmin ):
    fields = [ 'area', 'name' ]
    inlines = [ PartInline ]

class QuestionInline( admin.TabularInline ):
    model = Question
    extra = 3

class PartAdmin( admin.ModelAdmin ):
    fields = [ 'name', 'quantity', 'weight' ]
    inlines = [ QuestionInline ]

admin.site.register( Area )
admin.site.register( Test, TestAdmin )
admin.site.register( Part, PartAdmin )
