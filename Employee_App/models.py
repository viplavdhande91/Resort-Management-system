from django.db import models
from django.contrib.admin import widgets
import datetime
from django.contrib import admin
# Create your models here.
from django.conf import settings
from django.utils.safestring import mark_safe
from . import choices
# Create your models here.
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

#years field in all models

year_dropdown = []
for y in range(2018, (datetime.datetime.now().year + 80)):
    year_dropdown.append((y, y))



class Employee_name(models.Model):
    Employee_name = models.CharField(max_length=100)


    def __str__(self):              # for returning object name on saving notfication
        return self.Employee_name

    class Meta:
        verbose_name = "Employee_name"
        verbose_name_plural = "Employee_names"
        db_table = " Employee_name"


   
        

#standard employee names in all models

class Employee(models.Model): 
    Employee_name = models.ForeignKey(Employee_name,on_delete=models.PROTECT)
    Employee_Photo = models.ImageField(blank=True,null=True,upload_to="Employee_Photos",)
    Employee_Mobile=models.CharField(max_length=25,null=True,blank=True)
    Employee_Email=models.EmailField(max_length=254,blank=True)


    Bank_Account = models.CharField(max_length=100,null=True,blank=True)
    Working_or_NotWorking =models.BooleanField()
    IdProof = models.ImageField(blank=True,null=True,upload_to="Employee_Id_Proofs",)
    Date_of_join=models.DateField()
    Date_of_leave=models.DateField(blank=True,null=True)


    role_designation=models.CharField(max_length=100,choices=choices.ROLE_DESIGNATION, default=None)
   # role_id = models.IntegerField(null=True,blank=True)  
    Living_Adress = models.TextField(max_length=600,blank=True)
    created_Entry_date = models.DateTimeField(auto_now=True,editable=False)
     
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        db_table = " Employee"

   
    
    def image_tag(self):
        if self.Employee_Photo:
            return mark_safe('<img src="%s" style="width: 75px; height:100px;" />' % self.Employee_Photo.url)
        else:
            return 'No Image added'
    image_tag.short_description = 'Image'
     

    def image_tag_idproof(self):
        if self.IdProof:
            return mark_safe('<img src="%s" style="width: 100px; height:75px;" />' % self.IdProof.url)
        else:
            return 'No Id Proof added'
    image_tag_idproof.short_description = 'Image Id proof'


    def __str__(self):            
        return str(self.Employee_name)

   # def __str__(self):                  # for returning object name on saving notfication
    #    return "%s":"%d" % (self.Employee_name,self.Employee_id)
       

 
'''
for each in Employee.objects.all():
    Employee_name_choices.add((each.Employee_name,each.Employee_name))    
'''

class Roles(models.Model):

    role_id = models.IntegerField(unique =True)
    role_designation=models.CharField(max_length=100,choices=choices.ROLE_DESIGNATION, default=None)
    Basic_Salary=models.FloatField()
    no_of_Employees =models.IntegerField()
    created_Entry_date = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):            
        return self.role_designation
        

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        db_table = " Role"        
  
# derived models from here
class Leave(models.Model):
   
    Employee_name = models.ForeignKey(Employee_name,on_delete=models.PROTECT)

    From_Date=models.DateField()
    To_Date=models.DateField(blank=True,null=True,editable=True)
    no_of_Days=models.IntegerField(blank=True,null=True,editable=False)
    year = models.PositiveIntegerField(('year'), choices=year_dropdown, default=datetime.datetime.now().year)

    month = models.PositiveIntegerField('Month', choices=choices.MONTHS)
    
    reason_of_leave = models.TextField(max_length=600,blank=True)
    created_Entry_date = models.DateTimeField(auto_now=True,editable=False)



    def __str__(self):            
        return str(self.Employee_name)
     
    class Meta:
        verbose_name = "Leave"
        verbose_name_plural = "Leaves"
        db_table = "Leave"




class Standard_Salaries(models.Model):

    Employee_name = models.ForeignKey(Employee_name,on_delete=models.PROTECT)
    Basic_Salary_Per_Month=models.FloatField()
    Per_Day=models.FloatField()
    role_designation=models.CharField(max_length=100,choices=choices.ROLE_DESIGNATION, default=None)
    PF=models.FloatField(blank=True,null=True)
    Notes = models.TextField(max_length=1000,blank=True)
    created_Entry_date = models.DateTimeField(auto_now=True,editable=False)


    def __str__(self):            
        return str(self.Employee_name)
     
    class Meta:
        verbose_name = "Standard_Salary"
        verbose_name_plural = "Standard_Salaries"
        db_table = " Standard_Salary"



class Salary_Status(models.Model):

    Employee_name = models.ForeignKey(Employee_name,on_delete=models.PROTECT)
    role_designation=models.CharField(max_length=100,choices=choices.ROLE_DESIGNATION, default=None)
    month = models.PositiveIntegerField('Month',choices=choices.MONTHS)
    year = models.PositiveIntegerField(('year'),choices=year_dropdown, default=datetime.datetime.now().year)

    Salary_recieved_date=models.DateTimeField()
    Sal_status=models.CharField(max_length=100,choices=choices.STATUS, default=None)
    Money_To_Give=models.FloatField(blank=True,null=True,default=0)
    Money_To_Take=models.FloatField(blank=True,null=True,default=0)
    Cleared_or_Notcleared =models.BooleanField()



    Details = models.TextField(max_length=1000,blank=True)

    created_Entry_date = models.DateTimeField(auto_now=True,editable=False)



    def __str__(self):            
        return str(self.Employee_name)
     
    class Meta:
        verbose_name = "Salary_Status"
        verbose_name_plural = "Salary_Statuses"
        db_table = " Salary_Status"

class Advance_amount(models.Model):
    Employee_name = models.ForeignKey(Employee_name,on_delete=models.PROTECT)


    month = models.PositiveIntegerField('Month', choices=choices.MONTHS)
    year = models.PositiveIntegerField(('year'),  choices=year_dropdown, default=datetime.datetime.now().year)

    Advance_Amount_Taken = models.FloatField()
    Whole_Or_Partial_Amount_Paid_in_Middle = models.FloatField(blank=True,null=True)

    Advance_Taken_Date = models.DateTimeField()
    Cleared_or_Notcleared =models.BooleanField()

    #dues=models.DecimalField(max_digits=12, decimal_places=2,editable =False)
    created_Entry_date = models.DateTimeField(auto_now=True,editable=False)



    def __str__(self):            
        return str(self.Employee_name)

    class Meta:
        db_table = "Advance_amount"
     



class Attendance(models.Model):
    Employee_name = models.ForeignKey(Employee_name,on_delete=models.PROTECT)
    Date=models.DateField()
    Present_Absent =models.BooleanField()
    Time_in =models.DateTimeField(blank=True,null=True)
    Time_Out =models.DateTimeField(blank=True,null=True)
    year = models.PositiveIntegerField(('year'),  choices=year_dropdown, default=datetime.datetime.now().year)
    month = models.PositiveIntegerField('Month', choices=choices.MONTHS)

    Attnd_status=models.PositiveIntegerField('Attend_status',choices=choices.ATTENDANCE_STATUS)
    
    created_Entry_date = models.DateTimeField(auto_now=True,editable=False)



    
    def __str__(self):            
        return str(self.Employee_name)

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        db_table = "Attendance"


