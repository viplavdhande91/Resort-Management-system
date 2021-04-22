from .models import *
from django.db import models
import mysql.connector
from mysql.connector.cursor import MySQLCursor

#months choices

January,February,March,April,May,June,July,August,September,October,November,December =range(1,13,1)
    
MONTHS = [
    (January, 'January'),
    (February, 'February'),
    (March, 'March'),
    (April, 'April'),
    (May, 'May'),
    (June, 'June'),
    (July, 'July'),
    (August, 'August'),
    (September, 'September'),
    (October, 'October'),
    (November, 'November'),
    (December, 'December'),
    
    ]

# model=salary status

PAID ='PAID'
NOTPAID ='NOTPAID'

    
STATUS = [
    (PAID, 'PAID'),
    (NOTPAID, 'NOTPAID'),]

#model= Role         role_designation 


MANAGER ='MANAGER'
CAPTAIN ='CAPTAIN'
WAITER ='WAITER'
HELPER ='HELPER'
CLEANER='CLEANER'
WATCHMAN='WATCHMAN'
KITCHEN_SUPERVISOR= 'KITCHEN_SUPERVISOR'

    
ROLE_DESIGNATION = [
    (MANAGER, 'MANAGER'),
    (CAPTAIN, 'CAPTAIN'),
    (WAITER, 'WAITER'),
    (HELPER, 'HELPER'),
    (CLEANER, 'CLEANER'),
    (WATCHMAN, 'WATCHMAN'),
    (KITCHEN_SUPERVISOR, 'KITCHEN_SUPERVISOR'),
    ]

#model=Attendance           status
LEAVE,PRESENT   = range(2)



ATTENDANCE_STATUS = [
    (LEAVE, 'LEAVE'),
     (PRESENT, 'PRESENT'),]




Lakhan_Bhalerao ='Lakhan Bhalerao'
Manoj_Chumbale = 'Manoj Chumbale'
Devidas_Mahale ='Devidas Mahale'


Employee_name_choices =[(Lakhan_Bhalerao, 'Lakhan Bhalerao'),

(Manoj_Chumbale, 'Manoj Chumbale'),
(Devidas_Mahale, 'Devidas Mahale'),










]