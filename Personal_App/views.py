from django.shortcuts import render
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from django.http import HttpResponseRedirect
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
# Create your views here.
from django.shortcuts import render,redirect




@login_required(login_url='/tables/login/')
def todolist_index(request): #the index view
    return redirect('/tables/Personal_App/to_do_list/')

