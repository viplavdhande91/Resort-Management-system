from django.conf.urls import url
from django.urls import path
from . import views,views_advance,views_attendance,views_salary
from django.contrib import admin




urlpatterns = [
    path('',views.home,name='home'),
    path('tables/',views.djangoadmin,name='djangoadmin'),
    path('tables/Employee_App/',views.employee_link,name='employee_link'),
    path('tables/Personal_App/',views.personal_app,name='personal_app'),
    path('tables/Employee_App/leave/',views.leave_url,name='leave_url'),
    path('tables/Employee_App/salary_status/',views.Salary_Status_url,name='Salary_Status_url'),
    path('tables/Employee_App/Standard_Salaries/',views.Standard_Salaries,name='Standard_Salaries'),



    path('asterisk/',views.people,name='people'),


    path('unsettled_Advance/',views_advance.unsettled_Advance,name='unsettled_Advance'),
    path('Advance_Amount/',views_advance.Advance_Amount,name='Advance_Amount'),


    path('distrubuted_total_Advance_template/',views_advance.distrubuted_total_Advance_template,name='distrubuted_total_Advance_template'),
    path('distrubuted_total_Advance_template/distrubuted_total_Advance',views_advance.distrubuted_total_Advance,name='distrubuted_total_Advance'),

    path('Advance_Amount_year/',views_advance.Advance_Amount_year,name='Advance_Amount_year'),
    path('Advance_Amount_year/Advance_Amount_year_action',views_advance.Advance_Amount_year_action,name='Advance_Amount_year_action'),
   
    path('Advance_Amount_month_total_stats/',views_advance.Advance_Amount_month_total_stats,name='Advance_Amount_month_total_stats'),
    path('Advance_Amount_month_total_stats/Advance_Amount_month_total_stats_action',views_advance.Advance_Amount_month_total_stats_action,name='Advance_Amount_month_total_stats_action'),

    
    path('this_month_Salary_template_edit/',views_salary.this_month_Salary_template_edit,name='this_month_Salary_template_edit'),

    path('this_month_Salary_template_edit/this_month_Salary_excel',views_salary.this_month_Salary_excel,name='this_month_Salary_excel'),

    path('this_month_Salary_template_edit/this_month_Salary_display',views_salary.this_month_Salary_display,name='this_month_Salary_display'),









    path('attendance_this_month/',views_attendance.attendance_this_month,name='attendance_this_month'),

    path('attendance_Of_Any_month/',views_attendance.attendance_Of_Any_month,name='attendance_Of_Any_month'),
    path('attendance_Of_Any_month/attendance_Of_Any_month1',views_attendance.attendance_Of_Any_month1,name='attendance_Of_Any_month1'),
    path('attendance/',views_attendance.attendance,name='attendance'),

    path('attendance_chart/',views_attendance.attendance_chart,name='attendance_chart'),









    

    ]




