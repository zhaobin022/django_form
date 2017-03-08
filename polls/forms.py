# -*- coding: utf-8 -*-
from django import forms
from polls.models import  *
from django.forms import widgets
from app01.models import *
from django.forms import ValidationError

from django.forms.forms import NON_FIELD_ERRORS


class HostModelForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]



class UserForm(forms.Form):
    username = forms.CharField(
        label='Your name',
        error_messages={'required':u"User name can't empty !","min_length":"can't less than five  "},
        widget=widgets.TextInput(attrs={"class":"c1"}),
        required=False,
    )

    password = forms.CharField(
        label='Passwod',
        error_messages={'required':u"password can't empty !"},
        widget=widgets.PasswordInput(),
        required=False,
    )


    email = forms.EmailField(
        label="You email",
        error_messages={
            'required': u'邮箱不能为空',
            'invalid': u'请输入正确的邮箱',
        },
        required = False,

    )

    host_list = forms.ChoiceField(
        required=False,

    )

    host_mul_list = forms.CharField(
        initial=[1,2],
        required=False,
        widget=widgets.SelectMultiple,
    )


    server_name = forms.CharField(
        label="server name",
        required=False,
    )


    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields["host_list"].choices = Host.objects.values_list("id","name")
        self.fields["host_list"].widget.choices = Host.objects.values_list("id","name")
        self.fields["host_list"].widget.attrs = {"class":"c2"}
        self.fields["host_mul_list"].widget.choices = Host.objects.values_list("id","name")




    def clean_server_name(self):
        host_count = Host.objects.filter(name=self.cleaned_data["server_name"]).count()

        if host_count:
            raise ValidationError("server_name already exist !",code="invalid")
        else:
            return self.cleaned_data["server_name"]



    def _clean_form(self):

        if self.cleaned_data['username'] == 'test' and self.cleaned_data['password'] == 'test':
            return self.cleaned_data
        else:
            self._errors[NON_FIELD_ERRORS] = self.error_class(['user name or password fail!!!!'])
            # raise ValidationError("user name or password fail!!!!")