from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, resolve_url

#django.contrib.auth import get_user_model

class User(AbstractUser):
    class GenderChices(models.TextChoices):
        MALE = "M","Male"   #DB에저장되는 값 ,실제 사용할 값
        FEMALE = "F","Female"
#r"^010-?[1-9]\d{4}-?\d{4}$"
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True) 
    phone_number = models.CharField(max_length=15,blank=True,validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1,blank=True,choices=GenderChices.choices)#,default=GenderChices.MALE
    avatar = models.ImageField(blank=True, upload_to = 'accounts/avatar/%Y/%m/%d')
    #help_text="48px크기 파일업로드") 나중에 validators
    
    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image",self.username)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def send_welcome_email(self):
#send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
        
        subject=render_to_string("accounts/welcome_email_subject.txt",{'user':self,})
        content=render_to_string("accounts/welcome_email_content.txt",{'user':self,})
        sender_email = settings.WELCOME_EMAIL_SENDER #보내는 사람
        send_mail(subject,content,send_mail,[self.email],fail_silently=False)


    # def save(self,*args,**kwargs):
    #     is_create = self.pk == None
    #     super().save(*args,**kwargs)
    #     if is_create:
