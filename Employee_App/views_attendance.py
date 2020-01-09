from django.shortcuts import render
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.
from functools import reduce
import pandas as pd
from io import BytesIO as IO
from django.http import HttpResponse
import xlsxwriter
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render
import mysql.connector
from mysql.connector.cursor import MySQLCursor
import datetime

# Create your views here.
import calendar
from .models import *
import itertools
from django.db.models import Q
from django.contrib.auth.decorators import login_required



@login_required(login_url='/tables/login/')
def attendance(request):
    return redirect('/tables/Employee_App/attendance/')




#tested function=working fine
@login_required(login_url='/tables/login/')
def attendance_this_month(request):

#for all data show i  dataframe
    pd.set_option('display.max_colwidth', -1)



    try:
        from io import BytesIO as IO # for modern python

    except ImportError:
        from io import StringIO as IO # for legacy python

#Attendance table  copy as it is and filter as per not_recived and sent status 

    copy1=Attendance.objects.all().values_list('Employee_name','Attnd_status', 'year','month',).filter(Q(Attnd_status=1) & Q(year=datetime.datetime.now().year) & Q(month=datetime.datetime.now().month)) #get either not_recieved or sent 
    dframe1 = pd.DataFrame(copy1, columns=['Employee_name','Present_Days', 'year','month',])

#group by non repeating for sum of items_names and not recieved number
    dframe1=dframe1.groupby(['Employee_name',]).agg({'Present_Days':'sum',}).reset_index()





#Attendance table  copy as it is and filter as per not_recived and sent status 

    copy2=Attendance.objects.all().values_list('Employee_name','Attnd_status', 'year','month',).filter(Q(Attnd_status=0) & Q(year=datetime.datetime.now().year) & Q(month=datetime.datetime.now().month)) #get either not_recieved or sent 
    dframe2 = pd.DataFrame(copy2, columns=['Employee_name','Absent_Days', 'year','month',])

    dframe2['Absent_Days']=dframe2['Absent_Days'].replace([0,], 1)



#group by non repeating for sum of items_names and not recieved number
    dframe2=dframe2.groupby(['Employee_name',]).agg({'Absent_Days':'sum',}).reset_index()



#join two dataframes on attribute=Employee name
     
    #combined two dataframes same columns
    dframe3 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe2, dframe1])
   



#insertion logic of days of this month
    now = datetime.datetime.now()
    This_month_days= calendar.monthrange(now.year, now.month)[1]

    repeat_var =list(itertools.repeat(This_month_days, dframe3.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)


    dframe3['Total_Days_Of_This_Month'] = repeat_var

#insertion logic for month + year column
    month_year = str(datetime.datetime.now().month) +','+ str(datetime.datetime.now().year)

    repeat_var1 =list(itertools.repeat(month_year, dframe3.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)

    dframe3['Current_month'] = repeat_var1




#adding 0 at missing entries
   
    dframe3 = dframe3.fillna(0)




#rearanging dataframe columns    
    dframe3 = dframe3[['Employee_name','Current_month','Total_Days_Of_This_Month','Absent_Days','Present_Days',]]




    dframe3 = dframe3.to_html(classes=["table-bordered", "table-striped", "table-hover",])
    context = { 'dframerender2': dframe3}
 

    return render(request, 'render_output_to_html/output2.html',context,)









#tested function=working fine
@login_required(login_url='/tables/login/')
def attendance_Of_Any_month(request):
    return render(request, 'forms_template/attendance_edit.html',)



 #tested function=working fine
@login_required(login_url='/tables/login/')
def attendance_Of_Any_month1(request):
    if request.method == "POST":
        #monthvarnum = request.GET.get('sel')
#capturing values from user input
        monthvarnum = request.POST.get('Select')
        monthvarnum =int(monthvarnum)
        
        yearvarnum = request.POST.get('year')
        yearvarnum =int(yearvarnum)

        #for all data show i  dataframe
        pd.set_option('display.max_colwidth', -1)

        try:
            from io import BytesIO as IO # for modern python

        except ImportError:
            from io import StringIO as IO # for legacy python


    
#Attendance table  copy as it is and filter as per not_recived and sent status 

        copy1=Attendance.objects.all().values_list('Employee_name','Attnd_status', 'year','month',).filter(Q(Attnd_status=1) & Q(year=yearvarnum) & Q(month=monthvarnum)) #get either not_recieved or sent 
        dframe1 = pd.DataFrame(copy1, columns=['Employee_name','Present_Days', 'year','month',])

#group by non repeating for sum of items_names and not recieved number
        dframe1=dframe1.groupby(['Employee_name',]).agg({'Present_Days':'sum',}).reset_index()





#Attendance table  copy as it is and filter as per not_recived and sent status 

        copy2=Attendance.objects.all().values_list('Employee_name','Attnd_status', 'year','month',).filter(Q(Attnd_status=0) & Q(year=yearvarnum) & Q(month=monthvarnum)) #get either not_recieved or sent 
        dframe2 = pd.DataFrame(copy2, columns=['Employee_name','Absent_Days', 'year','month',])

        dframe2['Absent_Days']=dframe2['Absent_Days'].replace([0,], 1)



#group by non repeating for sum of items_names and not recieved number
        dframe2=dframe2.groupby(['Employee_name',]).agg({'Absent_Days':'sum',}).reset_index()



#join two dataframes on attribute=Employee name
     
    #combined two dataframes same columns
        dframe3 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe2, dframe1])
   



#insertion logic of days of this month
      #  now = datetime.datetime
        This_month_days= calendar.monthrange(yearvarnum,monthvarnum)[1]

        repeat_var =list(itertools.repeat(This_month_days, dframe3.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)


        dframe3['Total_Days_Of_This_Month'] = repeat_var



#adding 0 at missing entries
   
        dframe3 = dframe3.fillna(0)




#rearanging dataframe columns    
        dframe3 = dframe3[['Employee_name','Total_Days_Of_This_Month','Present_Days','Absent_Days']]
    

    # my "Excel" file, which is an in-memory output file (buffer) 
# for the new workbook
        excel_file = IO()

        xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')


        dframe3.to_excel(xlwriter, 'This_month_Attendance')

        workbook  = xlwriter.book
        worksheet = xlwriter.sheets['This_month_Attendance']

        worksheet.set_column('B:C',25)

        worksheet.set_column('D:E',25)



        xlwriter.save()
        xlwriter.close()
# important step, rewind the buffer or when it is read() you'll get nothing
# but an error message when you try to open your zero length file in Excel
        excel_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# set the file name in the Content-Disposition header
        response['Content-Disposition'] = 'attachment; filename= Custom_Attendance_Month_Salary.xlsx'    


    #dframe2.to_csv(path_or_buf=response,index=False,) 
    
    return response



@login_required(login_url='/tables/login/')
def attendance_chart(request):
    pass