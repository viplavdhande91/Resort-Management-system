from django.db import models
from django.contrib.admin import widgets
import datetime
from django.contrib import admin
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from . import choices1
from django.utils import timezone

# Create your models here.
class ToDoCategory(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    
    def __str__(self):
        return self.name #name to be shown when called


    class Meta:
        db_table = "ToDoCategory"
        verbose_name = "ToDoCategory"
        verbose_name_plural = "ToDoCategories"    



Category_choices=set()
'''
for each in ToDoCategory.objects.all():
    Category_choices.add((each.name,each.name))    

'''

class My_Expenses(models.Model):
    category = models.CharField(max_length=100,choices=choices1.Category_choices, default=None)

    Trxn_Amt=models.FloatField()
    Created_On = models.DateTimeField()
    Paid_to = models.CharField(max_length=100)
    Description = models.TextField(max_length=1000,blank=True)

    created_Entry_date = models.DateField(default=datetime.date.today,editable=False)

    class Meta:
        verbose_name = "My_Expense"
        verbose_name_plural = "My_Expenses"
        db_table = " My_Expense"



class To_do_List(models.Model): #Todolist able name that inherits models.Model
    category = models.CharField(max_length=100,choices=choices1.Category_choices, default=None)
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    Time=models.TimeField(blank=True,null=True)

    Done_or_Not_Done =models.BooleanField()
    created = models.DateTimeField(auto_now=True,editable=False)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    
   
    def __str__(self):
        return self.title #name to be shown when called


    class Meta:
        verbose_name = "To_do_List"
        verbose_name_plural = "To_do_Lists"
        db_table = " To_do_List"
         
