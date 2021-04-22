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

'''
@login_required(login_url='/mysite/login/')
def index(request):
    return render(request, 'index.html')
'''


#function tested #working properly
@login_required(login_url='/login/')
def unsettled_Advance(request):
#for all data show i  dataframe
    pd.set_option('display.max_colwidth', -1)

    try:
        from io import BytesIO as IO # for modern python

    except ImportError:
        from io import StringIO as IO # for legacy python

    unsettled=Advance_amount.objects.all().values_list('Employee_name','Advance_Amount_Taken','Cleared_or_Notcleared' ).filter(Cleared_or_Notcleared=0 ) #get either  not cleared
    dframe00 = pd.DataFrame(unsettled, columns=['Employee_name','Total_Advance_Amount_Taken','Cleared_or_Notcleared?'])

    #group by non repeating for sum of items_names and not recieved number
    dframe1=dframe00.groupby(['Employee_name',]).agg({'Total_Advance_Amount_Taken':'sum',}).reset_index()




#add column Whole_Or_Partial_Amount_Paid_in_Middle into dframe2
    

    copy2=Advance_amount.objects.all().values_list('Employee_name','Whole_Or_Partial_Amount_Paid_in_Middle').filter(Cleared_or_Notcleared =0) #get either not_recieved or sent 
        
    dframe2 = pd.DataFrame(copy2, columns=['Employee_name','Whole_Or_Partial_Amount_Paid_in_Middle',])


    dframe2=dframe2.groupby(['Employee_name',]).agg({'Whole_Or_Partial_Amount_Paid_in_Middle':'sum',}).reset_index()


   
   
#join two dataframes on attribute=Employee name     
#combined two dataframes same columns
    dframe2 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe2, dframe1])



    dframe2['Remaining_Amt'] = dframe2['Total_Advance_Amount_Taken'] - dframe2['Whole_Or_Partial_Amount_Paid_in_Middle']
 
#insertion logic of cleared or not
    dframe00=dframe00.drop(['Total_Advance_Amount_Taken',], axis=1) #dropping few column names

    dframe00=dframe00.groupby('Employee_name').prod()   #grouping data and multplication on cleared_not_cleared column
        
    for col in dframe00.columns[dframe00.dtypes == 'bool']:
            dframe00[col] = dframe00[col].map({True: 'Yes', False: 'No'})



 
   
#join two dataframes on attribute=Employee name     
#combined two dataframes same columns
    dframe3 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe00, dframe2])


    
#rearanging dataframe columns    
    dframe3 = dframe3[['Employee_name','Total_Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle','Remaining_Amt','Cleared_or_Notcleared?',]]
    
    dframe3 = dframe3.to_html(classes=["table-bordered", "table-striped", "table-hover",])
    context = { 'object_list1': dframe3}
 

    return render(request, 'render_output_to_html/output1.html',context,)



   







#tested function=working fine
@login_required(login_url='/tables/login/')
def distrubuted_total_Advance_template(request):
    return render(request, 'forms_template/advance_amount_edit.html',)



#tested function=working fine
@login_required(login_url='/tables/login/')
def Advance_Amount(request):
    return redirect('/tables/Employee_App/advance_amount/')



#tested function=working fine
@login_required(login_url='/tables/login/')
def distrubuted_total_Advance(request):
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

        copy1=Advance_amount.objects.all().values_list('Employee_name','Advance_Amount_Taken','year','month','Cleared_or_Notcleared').filter( Q(year=yearvarnum) & Q(month=monthvarnum ) ) #get either not_recieved or sent 
        dframe00 = pd.DataFrame(copy1, columns=['Employee_name','Total_Advance_Amount_Taken', 'year','month','Advance_amount_Cleared?'])
    
        #group by non repeating for sum of items_names and not recieved number
        dframe1=dframe00.groupby(['Employee_name',]).agg({'Total_Advance_Amount_Taken':'sum',}).reset_index()

      #  dframe1=dframe1.groupby(['Employee_name',]).agg({'Advance_Amount_Paid_in_Middle':'sum',}).reset_index()


#insertion logic of month value repeatedly in dataframe
        This_month_name= monthvarnum

        repeat_var_month =list(itertools.repeat(This_month_name, dframe1.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)


        dframe1['Month'] = repeat_var_month



#insertion logic of year value repeatedly in dataframe
        This_year_name= yearvarnum

        repeat_var_year =list(itertools.repeat(This_year_name, dframe1.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)


        dframe1['Year'] = repeat_var_year




#insertion logic of cleared or not
        dframe00=dframe00.drop(['Total_Advance_Amount_Taken', 'year','month',], axis=1) #dropping few column names

        dframe00=dframe00.groupby('Employee_name').prod()   #grouping data and multplication on cleared_not_cleared column
        
        for col in dframe00.columns[dframe00.dtypes == 'bool']:
            dframe00[col] = dframe00[col].map({True: 'Yes', False: 'No'})
#group by non repeating for sum of items_names and not recieved number
        


   
#join two dataframes on attribute=Employee name     
#combined two dataframes same columns
        dframe2 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe00, dframe1])


#add column Whole_Or_Partial_Amount_Paid_in_Middle into dframe2
    

        copy2=Advance_amount.objects.all().values_list('Employee_name','Whole_Or_Partial_Amount_Paid_in_Middle').filter( Q(year=yearvarnum) & Q(month=monthvarnum ) ) #get either not_recieved or sent 
        
        dframetemp = pd.DataFrame(copy2, columns=['Employee_name','Whole_Or_Partial_Amount_Paid_in_Middle',])


        dframetemp=dframetemp.groupby(['Employee_name',]).agg({'Whole_Or_Partial_Amount_Paid_in_Middle':'sum',}).reset_index()


   
   
#join two dataframes on attribute=Employee name     
#combined two dataframes same columns
        dframe2 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe2, dframetemp])



        dframe2['Remaining_Amt'] =dframe2['Total_Advance_Amount_Taken'] - dframe2['Whole_Or_Partial_Amount_Paid_in_Middle']
 



#rearanging dataframe columns    
        dframe2 = dframe2[['Employee_name','Year','Month','Total_Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle','Remaining_Amt','Advance_amount_Cleared?',]]



# my "Excel" file, which is an in-memory output file (buffer) 
# for the new workbook
        excel_file = IO()

        xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')


        dframe2.to_excel(xlwriter, 'Advanced_Amount_Statistics')

        workbook  = xlwriter.book
        worksheet = xlwriter.sheets['Advanced_Amount_Statistics']

        worksheet.set_column('B:B',25)

        worksheet.set_column('C:D',6)
        worksheet.set_column('E:E',30)
        worksheet.set_column('F:F',40)
        worksheet.set_column('G:H',33)



        xlwriter.save()
        xlwriter.close()
# important step, rewind the buffer or when it is read() you'll get nothing
# but an error message when you try to open your zero length file in Excel
        excel_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# set the file name in the Content-Disposition header
        response['Content-Disposition'] = 'attachment; filename= MonthWise_Statistics_Of_Advanced_Amount.xlsx'    


    #dframe2.to_csv(path_or_buf=response,index=False,) 
    
    return response





#tested function=working fine
@login_required(login_url='/tables/login/')
def Advance_Amount_year(request):
    return render(request, 'forms_template/advance_amount_year.html',)




@login_required(login_url='/tables/login/')
def Advance_Amount_year_action(request):
      if request.method == "POST":
        #monthvarnum = request.GET.get('sel')
#capturing values from user input
        
        yearvarnum = request.POST.get('year')
        yearvarnum =int(yearvarnum)

        #for all data show i  dataframe
        pd.set_option('display.max_colwidth', -1)

        try:
            from io import BytesIO as IO # for modern python

        except ImportError:
            from io import StringIO as IO # for legacy python

        
#Attendance table  copy as it is and filter as per not_recived and sent status 

        copy1=Advance_amount.objects.all().values_list('Employee_name','Advance_Amount_Taken','year','Cleared_or_Notcleared').filter( year=yearvarnum ) #get either not_recieved or sent 
        dframe00 = pd.DataFrame(copy1, columns=['Employee_name','Total_Advance_Amount_Taken', 'year','Advance_amount_Cleared?'])
    
        #group by non repeating for sum of items_names and not recieved number
        dframe1=dframe00.groupby(['Employee_name',]).agg({'Total_Advance_Amount_Taken':'sum',}).reset_index()

        

#insertion logic of year value repeatedly in dataframe
        This_year_name= yearvarnum

        repeat_var_year =list(itertools.repeat(This_year_name, dframe1.Employee_name.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)


        dframe1['Year'] = repeat_var_year

        
#insertion logic of cleared or not
        dframe00=dframe00.drop(['Total_Advance_Amount_Taken', 'year',], axis=1) #dropping few column names

        dframe00=dframe00.groupby('Employee_name').prod()   #grouping data and multplication on cleared_not_cleared column
        
        for col in dframe00.columns[dframe00.dtypes == 'bool']:
            dframe00[col] = dframe00[col].map({True: 'Yes', False: 'No'})

#group by non repeating for sum of items_names and not recieved number
        
   
#join two dataframes on attribute=Employee name     
#combined two dataframes same columns
        dframe2 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe00, dframe1])

#add column Whole_Or_Partial_Amount_Paid_in_Middle into dframe2
    

        copy2=Advance_amount.objects.all().values_list('Employee_name','Whole_Or_Partial_Amount_Paid_in_Middle').filter(year=yearvarnum ) #get either not_recieved or sent 
        
        dframetemp = pd.DataFrame(copy2, columns=['Employee_name','Whole_Or_Partial_Amount_Paid_in_Middle',])


        dframetemp=dframetemp.groupby(['Employee_name',]).agg({'Whole_Or_Partial_Amount_Paid_in_Middle':'sum',}).reset_index()


   
   
#join two dataframes on attribute=Employee name     
#combined two dataframes same columns
        dframe3 = reduce(lambda x,y: pd.merge(x,y, on=['Employee_name',], how='outer'), [dframe2, dframetemp])



        dframe3['Remaining_Amt'] =dframe3['Total_Advance_Amount_Taken'] - dframe3['Whole_Or_Partial_Amount_Paid_in_Middle']


        
#rearanging dataframe columns    
        dframe3 = dframe3[['Employee_name','Year','Total_Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle','Remaining_Amt','Advance_amount_Cleared?',]]

       
        
# my "Excel" file, which is an in-memory output file (buffer) 
# for the new workbook
        excel_file = IO()

        xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')


        dframe3.to_excel(xlwriter, 'Advanced_Amount_Statistics')

        workbook  = xlwriter.book
        worksheet = xlwriter.sheets['Advanced_Amount_Statistics']

        worksheet.set_column('B:B',25)

        worksheet.set_column('C:C',6)
        worksheet.set_column('D:E',30)
        worksheet.set_column('E:E',40)

        worksheet.set_column('F:G',28)


        xlwriter.save()
        xlwriter.close()
# important step, rewind the buffer or when it is read() you'll get nothing
# but an error message when you try to open your zero length file in Excel
        excel_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# set the file name in the Content-Disposition header
        response['Content-Disposition'] = 'attachment; filename= Yearwise_Statistics_Of_Advanced_Amount.xlsx'  

        return response  


    #dframe2.to_csv(path_or_buf=response,index=False,) 
    
      
      
    






#tested function=working fine
@login_required(login_url='/tables/login/')
def Advance_Amount_month_total_stats(request):
    return render(request, 'forms_template/advance_amount_month_total_stats.html',)




#tested function=working fine
@login_required(login_url='/tables/login/')
def Advance_Amount_month_total_stats_action(request):

    if request.method == "POST":
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

                
#Attendance table  copy as it is and filter as per not_recived and sent status 

        copy1=Advance_amount.objects.all().values_list('Advance_Amount_Taken','year','month','Cleared_or_Notcleared','Whole_Or_Partial_Amount_Paid_in_Middle').filter( Q(year=yearvarnum) & Q(month=monthvarnum ) ) #get either not_recieved or sent 
        dframe00 = pd.DataFrame(copy1, columns=['Total_Advance_Amount_Taken', 'year','month','Advance_amount_Cleared?','Whole_Or_Partial_Amount_Paid_in_Middle'])
    
#group by non repeating for sum of items_names and not recieved number
        dframe1=dframe00.groupby(['month',]).agg({'Total_Advance_Amount_Taken':'sum',}).reset_index()

      #  dframe1=dframe1.groupby(['Employee_name',]).agg({'Advance_Amount_Paid_in_Middle':'sum',}).reset_index()



#add column Whole_Or_Partial_Amount_Paid_in_Middle into dframe2
    

        copy2=Advance_amount.objects.all().values_list('month','Whole_Or_Partial_Amount_Paid_in_Middle').filter( Q(year=yearvarnum) & Q(month=monthvarnum) )#get either not_recieved or sent 
        
        dframe2 = pd.DataFrame(copy2, columns=['month','Whole_Or_Partial_Amount_Paid_in_Middle',])


        dframe2=dframe2.groupby(['month',]).agg({'Whole_Or_Partial_Amount_Paid_in_Middle':'sum',}).reset_index()


  
#join two dataframes on attribute=Employee name     
#combined two dataframes same columns
        dframe3 = reduce(lambda x,y: pd.merge(x,y, on=['month',], how='outer'), [dframe2, dframe1])

     
#insertion logic of year value repeatedly in dataframe
        This_year_name= yearvarnum

        repeat_var_year =list(itertools.repeat(This_year_name, dframe3.month.count()))           #list generation of repeated values it = itertools.repeat(no of items,no of times)


        dframe3['Year'] = repeat_var_year



        
#rearanging dataframe columns    
        dframe3 = dframe3[['month','Year','Total_Advance_Amount_Taken','Whole_Or_Partial_Amount_Paid_in_Middle',]]


        dframe3['is_total_amount_paid?'] = np.where(dframe3['Total_Advance_Amount_Taken']==dframe3['Whole_Or_Partial_Amount_Paid_in_Middle'], 'yes', 'no')

        dframe3 = dframe3.to_html(classes=["table-bordered", "table-striped", "table-hover",])
        context = { 'dframerender': dframe3}
 

        return render(request, 'render_output_to_html/output.html',context,)

































'''     
# my "Excel" file, which is an in-memory output file (buffer) 
# for the new workbook
        excel_file = IO()

        xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')


        dframe3.to_excel(xlwriter, 'Advanced_Amount_Statistics')

        workbook  = xlwriter.book
        worksheet = xlwriter.sheets['Advanced_Amount_Statistics']

        worksheet.set_column('B:C',10)

        worksheet.set_column('D:D',30)  
        worksheet.set_column('E:E',45)  
        worksheet.set_column('F:F',33)   
 
 

        xlwriter.save()
        xlwriter.close()
# important step, rewind the buffer or when it is read() you'll get nothing
# but an error message when you try to open your zero length file in Excel
        excel_file.seek(0)

        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# set the file name in the Content-Disposition header
        response['Content-Disposition'] = 'attachment; filename= Monthwise_Total_Statistics_Of_Advanced_Amount.xlsx'  

        return response  


    #dframe2.to_csv(path_or_buf=response,index=False,) 
    
      
      
    








'''