
from aspectometer.testing.models import Area, Test, Part, Question, Choice
from django.contrib import admin

class TestInline( admin.TabularInline ):
    model = Test
    extra = 3

class AreaAdmin( admin.ModelAdmin ):
    fields = [ 'name' ]
    inlines = [ TestInline ]

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

class ChoiceInline( admin.TabularInline ):
    model = Choice
    extra = 3

class QuestionAdmin( admin.ModelAdmin ):
    fields = [ 'content', 'weight' ]
    inlines = [ ChoiceInline ]

admin.site.register( Area, AreaAdmin )
admin.site.register( Test, TestAdmin )
admin.site.register( Part, PartAdmin )
admin.site.register( Question, QuestionAdmin )
