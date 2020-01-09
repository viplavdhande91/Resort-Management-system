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








#tested function=working fine
@login_required(login_url='/tables/login/')
def this_month_Salary_template_edit(request):
    return render(request, 'forms_template/salary_current_month_edit.html',)




@login_required(login_url='/tables/login/')
def this_month_Salary_excel(request):
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
#Table check1  query
        curr_att=Attendance.objects.all().values_list('Employee_name','Attnd_status', 'year','month',).filter(Q(Attnd_status=1)& Q(year=yearvarnum) & Q(month=monthvarnum)) #get either not_recieved or sent 
        dframe1 = pd.DataFrame(curr_att, columns=['Employee_name','Present_Days', 'year','month',])

           
#group by non repeating for sum of items_names and not recieved number
        dframe1=dframe1.groupby(['Employee_name',]).agg({'Present_Days':'sum',}).reset_index()




#dframe_attendance1['month']=datetime.datetime.now().month
#taking per_day attribute from Standard_Salaries table
#Table check2  query

        per_day=Standard_Salaries.objects.all().values_list('Employee_name','role_designation','Basic_Salary_Per_Month', 'Per_Day',)
        dframe2 = pd.DataFrame(per_day, columns=['Employee_name','role_designation','Basic_Salary_Per_Month', 'Per_Day',])






#CUT THE ADVANCE AMOUNT FROM SALARY LOGIC
#Table check3  query

        unsettled=Advance_amount.objects.all().values_list('Employee_name','Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle' ).filter(Cleared_or_Notcleared=0 ) #get either  not cleared
        dframe3 = pd.DataFrame(unsettled, columns=['Employee_name','Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle'])




    #group by non repeating for sum of items_names and not recieved number
        dframe3=dframe3.groupby(['Employee_name',]).agg({'Advance_Amount_Taken':'sum','Whole_Or_Partial_Amount_Paid_in_Middle':'sum'}).reset_index()

   



#Table check4  query

        money_givetake=Salary_Status.objects.all().values_list('Employee_name','Money_To_Give','Money_To_Take' ).filter(Cleared_or_Notcleared=0 ) #get either  not cleared
        dframe4 = pd.DataFrame(money_givetake, columns=['Employee_name','Money_To_Give','Money_To_Take',])




    #group by non repeating for sum of items_names and not recieved number
        dframe4=dframe4.groupby(['Employee_name',]).agg({'Money_To_Give':'sum','Money_To_Take':'sum'}).reset_index()

   



#combined two dataframes same columns
        dframefinal = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe1,dframe2,dframe3,dframe4])
   
    
        dframefinal['Present_Days'] = dframefinal['Present_Days'].astype(float)

        dframefinal['Salary_of_Month_Without_Cut'] = (dframefinal['Present_Days'] * dframefinal['Per_Day'])






# combining dframefinal to dframe_adv
       # dframefinal2 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe_adv3, dframefinal])
     

        dframefinal = dframefinal.replace('nan', np.nan).fillna(0)



       
#insertion logic for month + year column
        month_year = str(monthvarnum) +'th Month of '+ str(yearvarnum)
  
        repeat_var1 =list(itertools.repeat(month_year, dframefinal.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)

        dframefinal['Current_month'] = repeat_var1

 #new attribute salary after cutting money 

        dframefinal['Salary_of_Month_With_Cut'] = dframefinal['Salary_of_Month_Without_Cut'] - dframefinal['Advance_Amount_Taken']

        dframefinal['Salary_of_Month_With_Cut'] = dframefinal['Salary_of_Month_With_Cut'] - (dframefinal['Money_To_Take'] - dframefinal['Money_To_Give'])



        dframefinal['Salary_of_Month_With_Cut']  =dframefinal['Salary_of_Month_With_Cut'] + dframefinal['Whole_Or_Partial_Amount_Paid_in_Middle'] 


        
 


  #rearanging dataframe columns    
        dframefinal = dframefinal[['Employee_name','role_designation','Current_month','Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle','Money_To_Give','Money_To_Take','Basic_Salary_Per_Month','Per_Day','Present_Days','Salary_of_Month_Without_Cut','Salary_of_Month_With_Cut']]
        
        dframefinal['Advance_Amount_Taken'] = dframefinal['Advance_Amount_Taken'].map('{:,.2f} INR.'.format)
        dframefinal['Whole_Or_Partial_Amount_Paid_in_Middle'] = dframefinal['Whole_Or_Partial_Amount_Paid_in_Middle'].map('{:,.2f} INR.'.format)


        dframefinal['Money_To_Give'] = dframefinal['Money_To_Give'].map('{:,.2f} INR.'.format)
        dframefinal['Money_To_Take'] = dframefinal['Money_To_Take'].map('{:,.2f} INR.'.format)

        dframefinal['Basic_Salary_Per_Month'] = dframefinal['Basic_Salary_Per_Month'].map('{:,.2f} INR.'.format)

        dframefinal['Per_Day'] = dframefinal['Per_Day'].map('{:,.2f} INR.'.format)

        dframefinal['Salary_of_Month_Without_Cut'] = dframefinal['Salary_of_Month_Without_Cut'].map('{:,.2f} INR.'.format)

        dframefinal['Salary_of_Month_With_Cut'] = dframefinal['Salary_of_Month_With_Cut'].map('{:,.2f} INR.'.format)


  
# my "Excel" file, which is an in-memory output file (buffer) 
# for the new workbook
        excel_file = IO()

        xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')


        dframefinal.to_excel(xlwriter, 'This_month_Salary')

        workbook  = xlwriter.book
        worksheet = xlwriter.sheets['This_month_Salary']

        worksheet.set_column('B:B',18)

        worksheet.set_column('C:C',15)
        worksheet.set_column('D:E',23)
        worksheet.set_column('F:F',40)

        worksheet.set_column('G:G',16)
        worksheet.set_column('H:H',20)
        worksheet.set_column('I:I',25)
        worksheet.set_column('J:J',13)

        worksheet.set_column('K:K',15)
        worksheet.set_column('L:L',30)
        worksheet.set_column('M:M',30)





        xlwriter.save()
        xlwriter.close()
# important step, rewind the buffer or when it is read() you'll get nothing
# but an error message when you try to open your zero length file in Excel
        excel_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# set the file name in the Content-Disposition header
        response['Content-Disposition'] = 'attachment; filename= This_month_Salary.xlsx'    


    #dframe2.to_csv(path_or_buf=response,index=False,) 
    
        return response














@login_required(login_url='/tables/login/')
def this_month_Salary_display(request):
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
#Table check1  query
        curr_att=Attendance.objects.all().values_list('Employee_name','Attnd_status', 'year','month',).filter(Q(Attnd_status=1)& Q(year=yearvarnum) & Q(month=monthvarnum)) #get either not_recieved or sent 
        dframe1 = pd.DataFrame(curr_att, columns=['Employee_name','Present_Days', 'year','month',])

           
#group by non repeating for sum of items_names and not recieved number
        dframe1=dframe1.groupby(['Employee_name',]).agg({'Present_Days':'sum',}).reset_index()




#dframe_attendance1['month']=datetime.datetime.now().month
#taking per_day attribute from Standard_Salaries table
#Table check2  query

        per_day=Standard_Salaries.objects.all().values_list('Employee_name','role_designation','Basic_Salary_Per_Month', 'Per_Day',)
        dframe2 = pd.DataFrame(per_day, columns=['Employee_name','role_designation','Basic_Salary_Per_Month', 'Per_Day',])






#CUT THE ADVANCE AMOUNT FROM SALARY LOGIC
#Table check3  query

        unsettled=Advance_amount.objects.all().values_list('Employee_name','Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle' ).filter(Cleared_or_Notcleared=0 ) #get either  not cleared
        dframe3 = pd.DataFrame(unsettled, columns=['Employee_name','Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle'])




    #group by non repeating for sum of items_names and not recieved number
        dframe3=dframe3.groupby(['Employee_name',]).agg({'Advance_Amount_Taken':'sum','Whole_Or_Partial_Amount_Paid_in_Middle':'sum'}).reset_index()

   



#Table check4  query

        money_givetake=Salary_Status.objects.all().values_list('Employee_name','Money_To_Give','Money_To_Take' ).filter(Cleared_or_Notcleared=0 ) #get either  not cleared
        dframe4 = pd.DataFrame(money_givetake, columns=['Employee_name','Money_To_Give','Money_To_Take',])




    #group by non repeating for sum of items_names and not recieved number
        dframe4=dframe4.groupby(['Employee_name',]).agg({'Money_To_Give':'sum','Money_To_Take':'sum'}).reset_index()

   



#combined two dataframes same columns
        dframefinal = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe1,dframe2,dframe3,dframe4])
   
    
        dframefinal['Present_Days'] = dframefinal['Present_Days'].astype(float)

        dframefinal['Salary_of_Month_Without_Cut'] = (dframefinal['Present_Days'] * dframefinal['Per_Day'])






# combining dframefinal to dframe_adv
       # dframefinal2 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe_adv3, dframefinal])
     

        dframefinal = dframefinal.replace('nan', np.nan).fillna(0)



       
#insertion logic for month + year column
        month_year = str(monthvarnum) +'th Month of '+ str(yearvarnum)
  
        repeat_var1 =list(itertools.repeat(month_year, dframefinal.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)

        dframefinal['Current_month'] = repeat_var1

 #new attribute salary after cutting money 

        dframefinal['Salary_of_Month_With_Cut'] = dframefinal['Salary_of_Month_Without_Cut'] - dframefinal['Advance_Amount_Taken']

        dframefinal['Salary_of_Month_With_Cut'] = dframefinal['Salary_of_Month_With_Cut'] - (dframefinal['Money_To_Take'] - dframefinal['Money_To_Give'])



        dframefinal['Salary_of_Month_With_Cut']  =dframefinal['Salary_of_Month_With_Cut'] + dframefinal['Whole_Or_Partial_Amount_Paid_in_Middle'] 


  #rearanging dataframe columns    
        dframefinal = dframefinal[['Employee_name','role_designation','Current_month','Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle','Money_To_Give','Money_To_Take','Basic_Salary_Per_Month','Per_Day','Present_Days','Salary_of_Month_Without_Cut','Salary_of_Month_With_Cut']]
        
        dframefinal['Advance_Amount_Taken'] = dframefinal['Advance_Amount_Taken'].map('{:,.2f} INR.'.format)
        dframefinal['Whole_Or_Partial_Amount_Paid_in_Middle'] = dframefinal['Whole_Or_Partial_Amount_Paid_in_Middle'].map('{:,.2f} INR.'.format)


        dframefinal['Money_To_Give'] = dframefinal['Money_To_Give'].map('{:,.2f} INR.'.format)
        dframefinal['Money_To_Take'] = dframefinal['Money_To_Take'].map('{:,.2f} INR.'.format)

        dframefinal['Basic_Salary_Per_Month'] = dframefinal['Basic_Salary_Per_Month'].map('{:,.2f} INR.'.format)

        dframefinal['Per_Day'] = dframefinal['Per_Day'].map('{:,.2f} INR.'.format)

        dframefinal['Salary_of_Month_Without_Cut'] = dframefinal['Salary_of_Month_Without_Cut'].map('{:,.2f} INR.'.format)

        dframefinal['Salary_of_Month_With_Cut'] = dframefinal['Salary_of_Month_With_Cut'].map('{:,.2f} INR.'.format)







        dframefinal = dframefinal.to_html(classes=["table-bordered", "table-striped", "table-hover",])
        context = { 'object_list333': dframefinal}


 

        return render(request, 'render_output_to_html/output3.html',context,)



   

