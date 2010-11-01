from django.contrib.auth.models import User, Group
from aspectometer.testing.models import Technology, Aspect, Part, Question, Choice
from django import forms

from django.contrib import admin
from django.db import models

class CustomGroupAdminForm( forms.ModelForm ):
    users_set = forms.ModelMultipleChoiceField( label = 'Users', queryset = User.objects.all(), required = False, help_text = "Group users" )

    class Meta:
        model = Group

class CustomGroupAdmin( admin.ModelAdmin ):
    form = CustomGroupAdminForm

    fields = ( 'name', 'users_set', 'permissions', )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('permissions',)

    def save_model( self, request, obj, form, change ):
        if not change:
            obj.save()

        obj.user_set.clear()
        for user in form.cleaned_data['users_set']:
            obj.user_set.add( user )
        obj.save()

    def get_form( self, request, obj = None, **kwargs ):
        if obj:
            self.form.base_fields['users_set'].initial = [ user.id for user in obj.user_set.all() ]
        return super( CustomGroupAdmin, self ).get_form( request, obj )

#
#

class AspectInline( admin.TabularInline ):
    model = Aspect
    extra = 3

class TechnologyAdmin( admin.ModelAdmin ):
    fields = [ 'name' ]
    inlines = [ AspectInline ]
    

class PartInline( admin.TabularInline ):
    model = Part
    extra = 3

class AspectAdmin( admin.ModelAdmin ):
    fields = [ 'technology', 'name' ]
    inlines = [ PartInline ]

    list_display = ( 'technology', 'name', )
    list_display_links = ( 'name', )

    list_filter = ( 'technology', )
    search_fields = ( 'name', )

class QuestionInline( admin.TabularInline ):
    model = Question
    extra = 3

class PartAdmin( admin.ModelAdmin ):
    fields = [ 'name', 'quantity', 'weight' ]
    list_display = ( 'technology', 'aspect', 'name', )
    list_display_links = ( 'name', )
    inlines = [ QuestionInline ]
    list_filter = ( 'aspect', )
    search_fields = ( 'name', )

class ChoiceInline( admin.TabularInline ):
    model = Choice
    extra = 3

class QuestionAdmin( admin.ModelAdmin ):
    fields = [ 'content', 'weight' ]
    inlines = [ ChoiceInline ]

admin.site.register( Technology, TechnologyAdmin )
admin.site.register( Aspect, AspectAdmin )
admin.site.register( Part, PartAdmin )
admin.site.register( Question, QuestionAdmin )
admin.site.unregister( Group )
admin.site.register( Group, CustomGroupAdmin )
