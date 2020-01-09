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
def home(request):
    return render(request, 'index.html',)


@login_required(login_url='/tables/login/')
def djangoadmin(request):
    return redirect('/tables/')



@login_required(login_url='/tables/login/')
def employee_link(request):
    return redirect('/tables/Employee_App/')




@login_required(login_url='/tables/login/')
def personal_app(request):
    return redirect('/tables/Personal_App/')



@login_required(login_url='/tables/login/')
def leave_url(request):
    return redirect('/tables/Employee_App/leave/')



@login_required(login_url='/tables/login/')
def Salary_Status_url(request):
    return redirect('/tables/Employee_App/salary_status/')






@login_required(login_url='/tables/login/')
def Standard_Salaries(request):
    return redirect('/tables/Employee_App/standard_salaries/')





@login_required(login_url='/tables/login/')
def people(request):
	pd.set_option('display.max_colwidth', -1)
	unsettled=Advance_amount.objects.all().values_list('Employee_name','Advance_Amount_Taken','Cleared_or_Notcleared' ).filter(Cleared_or_Notcleared=0 )
	dframe00 = pd.DataFrame(unsettled, columns=['Employee_name','Total_Advance_Amount_Taken','Cleared_or_Notcleared?'])
	dframe001 = dframe00.to_html()
	context = { 'object_list': dframe001}
 

	return render(request, 'render_output_to_html/output.html',context,)


	








