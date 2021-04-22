from django.contrib import admin

# Register your models here.
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
from Employee_App.models import *
import decimal, csv
from django.http import HttpResponse
from django.db.models import F
from django.db.models import Q
import smtplib
import datetime
from. import models
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pandas as pd
import xlwt



LogEntry.objects.all().delete()
admin.site.unregister(Group)
# Register your models here.


class Employee_name_Admin(admin.ModelAdmin):
    list_display =['Employee_name']


        


admin.site.register(Employee_name, Employee_name_Admin)




class EmployeeAdmin(admin.ModelAdmin):
    #actions = [total_stock_seleted_entries_send_email]
    list_filter = ['role_designation','Date_of_join','Working_or_NotWorking']
    search_fields =['Employee_name','role_designation',]
    list_display = ('Employee_name','image_tag','Employee_Mobile','image_tag_idproof','Working_or_NotWorking','Employee_Email','Bank_Account','Date_of_join','Date_of_leave','role_designation','Living_Adress','created_Entry_date',)
    list_per_page = 5

    fieldsets = (

        ('Compulsary ', {
            'fields': (('Employee_name',) )
        }),

       

        ('Optional ', {
            'fields': (('Employee_Mobile','Employee_Email',),'Employee_Photo','Bank_Account','IdProof' )
        }),


        ('Optional : Date of Leave Only(Note:Could be filled After Permenant Leave of Employee Only) ', {
            'fields': (('Date_of_join','Date_of_leave','role_designation' ), )
        }),

        ('Compulsary : Tick:Currently Working , No Tick : Currently Not Working', {
            'fields': ('Working_or_NotWorking', )
        }),


        ('Optional :Upto 300 Words', {
            'fields': (('Living_Adress',), )
        }),


        
    )


    
admin.site.register(Employee, EmployeeAdmin)

#Leave actions

def fill_all_leave_date(modelAdmin, request, queryset):
    for x in queryset:
        diff = abs((x.From_Date-x.To_Date).days)
        x.no_of_Days = diff +1      
        x.save()

fill_all_leave_date.short_description = 'Calculate and Fill all leave dates'

class LeaveAdmin(admin.ModelAdmin):
    actions = [fill_all_leave_date]
    search_fields =['Employee_name','role_designation','month']
    ordering = ['Employee_name']
    list_display = ('Employee_name','From_Date','To_Date','no_of_Days','year','month','reason_of_leave','created_Entry_date',)
    list_per_page = 100
    
admin.site.register(Leave, LeaveAdmin)


class Standard_SalariesAdmin(admin.ModelAdmin):
    #actions = [total_stock_seleted_entries_send_email]
    search_fields =['Employee_name',]
    ordering = ['Employee_name']
    list_filter = ['role_designation',]

    list_display = ('Employee_name','Basic_Salary_Per_Month','role_designation','Per_Day','PF','Notes','created_Entry_date',)
    list_per_page = 100



admin.site.register(Standard_Salaries,Standard_SalariesAdmin)







class Salary_statusAdmin(admin.ModelAdmin):
    #actions = [total_stock_seleted_entries_send_email]
    search_fields =['Employee_name','month']
    ordering = ['Employee_name']
    list_filter = ['Salary_recieved_date','role_designation','Employee_name']

    list_display = ('Employee_name','role_designation','year','month','Salary_recieved_date','Sal_status','Money_To_Give','Money_To_Take','Cleared_or_Notcleared','Details','created_Entry_date',)
    list_per_page = 100
    change_list_template = "button_actions/SalaryModel_custom_button.html"



    
admin.site.register(Salary_Status,Salary_statusAdmin)
   


class Advance_amountAdmin(admin.ModelAdmin):
    #actions = [total_stock_seleted_entries_send_email]
    search_fields =['Employee_name','month']
    list_filter = ['Cleared_or_Notcleared','Advance_Taken_Date','Employee_name']


    ordering = ['Employee_name']
    list_display = ('Employee_name','month','year','Advance_Amount_Taken','Cleared_or_Notcleared','Advance_Taken_Date','Whole_Or_Partial_Amount_Paid_in_Middle','created_Entry_date')
    list_per_page = 100
    change_list_template = "button_actions/Advance_amount_custom_button.html"
    fieldsets = (
        (None, {
            'fields': ('Employee_name',)
        }),

        ('Add Advance Amount Given upto 2 Decimal Accuracy (Compulsary) e.g : 487.50 ', {
            'fields': (('Advance_Amount_Taken',), )
        }),


        ('Add Advance Amount Given Dates(Compulsary)', {
            'fields': (('month','year','Advance_Taken_Date'), )
        }),

        ('Compulsary: (NOTE : Tick=Advance Cleared ,NO Tick =Advance Not Cleared)', {
            'fields': (('Cleared_or_Notcleared',), )
        }),

         ('Compulsary: (NOTE :If Part of the amount paid by Employee then add paid Amount value here)', {
            'fields': (('Whole_Or_Partial_Amount_Paid_in_Middle'), )
        }),

        
    )
  

   # actions = [fill_Dues_of_Selected]


    
admin.site.register(Advance_amount, Advance_amountAdmin)





class RolesAdmin(admin.ModelAdmin):

        list_display = ('role_id','role_designation','Basic_Salary','no_of_Employees','created_Entry_date')
        list_filter = ['role_designation',]


    

admin.site.register(Roles, RolesAdmin)



class AttendanceAdmin(admin.ModelAdmin):
        search_fields =['Employee_name']


        list_display = ('Employee_name','Date','Present_Absent','Time_in','Time_Out','year','month','Attnd_status','created_Entry_date')
        list_filter = ['Date','Attnd_status','Employee_name']
        change_list_template = "button_actions/Attendance_custom_button.html"


        fieldsets = (
        (None, {
            'fields': ('Employee_name',)
        }),

        ('Add Attendance Times (Optional) e.g : 487.50', {
            'fields': ('Time_in','Time_Out')
        }),

        ('Add Attendance Date (Compulsary) ,Note: Tick= Present,No Tick= Absent',  {
            'fields': ('Date','year',('month','Attnd_status') ,'Present_Absent')
        }),


        
        
    )


    

admin.site.register(Attendance, AttendanceAdmin)


