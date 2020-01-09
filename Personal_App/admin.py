from django.contrib import admin

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import  Group
from django.contrib.auth.models import User

#import StringIO
from functools import reduce

import xlsxwriter
import io
import os
from django.urls import reverse
# Register your models here.
from django.db import models
from .models import *
import decimal, csv
from django.http import HttpResponse
from django.db.models import F
from django.db.models import Q
import smtplib
import datetime
from Personal_App.models import *
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pandas as pd
import xlwt


#LogEntry.objects.all().delete()


class My_ExpensesAdmin(admin.ModelAdmin):
	#actions = [total_stock_seleted_entries_send_email]
    list_filter = ['Created_On',]

    search_fields =['category','Paid_to',]
    #ordering = ['Employee_name']
    list_display = ('category','Trxn_Amt','Created_On','Paid_to','Description','created_Entry_date',)
    list_per_page = 100
   # change_list_template = "button_actions/Employee_custom_button.html
    

admin.site.register(My_Expenses, My_ExpensesAdmin)

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('category','Done_or_Not_Done',"title",'content','Time', "due_date",'created',)

      #actions = [total_stock_seleted_entries_send_email]
    list_filter = ['Done_or_Not_Done','due_date',]
    ordering = ['created']
    search_fields =['title',]
    list_per_page = 30

    fieldsets = (
        ('Note:(Compulsary)  ', {
            'fields': ('title','category','content')
        }),

        ('Optional ', {
            'fields': ('due_date','Time' )
        }),   

        ('Tick it after Task is Completed ', {
            'fields': ('Done_or_Not_Done', )
        }),   


        
    )


admin.site.register(To_do_List, TodoListAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)



admin.site.register(ToDoCategory,CategoryAdmin)


