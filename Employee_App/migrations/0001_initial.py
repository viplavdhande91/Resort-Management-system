# Generated by Django 2.2.2 on 2019-07-17 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Employee_name',
                'verbose_name_plural': 'Employee_names',
                'db_table': ' Employee_name',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField(unique=True)),
                ('role_designation', models.CharField(choices=[('MANAGER', 'MANAGER'), ('CAPTAIN', 'CAPTAIN'), ('WAITER', 'WAITER'), ('HELPER', 'HELPER'), ('CLEANER', 'CLEANER'), ('WATCHMAN', 'WATCHMAN'), ('KITCHEN_SUPERVISOR', 'KITCHEN_SUPERVISOR')], default=None, max_length=100)),
                ('Basic_Salary', models.FloatField()),
                ('no_of_Employees', models.IntegerField()),
                ('created_Entry_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'db_table': ' Role',
            },
        ),
        migrations.CreateModel(
            name='Standard_Salaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Basic_Salary_Per_Month', models.FloatField()),
                ('Per_Day', models.FloatField()),
                ('role_designation', models.CharField(choices=[('MANAGER', 'MANAGER'), ('CAPTAIN', 'CAPTAIN'), ('WAITER', 'WAITER'), ('HELPER', 'HELPER'), ('CLEANER', 'CLEANER'), ('WATCHMAN', 'WATCHMAN'), ('KITCHEN_SUPERVISOR', 'KITCHEN_SUPERVISOR')], default=None, max_length=100)),
                ('PF', models.FloatField(blank=True, null=True)),
                ('Notes', models.TextField(blank=True, max_length=1000)),
                ('created_Entry_date', models.DateTimeField(auto_now=True)),
                ('Employee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employee_App.Employee_name')),
            ],
            options={
                'verbose_name': 'Standard_Salary',
                'verbose_name_plural': 'Standard_Salaries',
                'db_table': ' Standard_Salary',
            },
        ),
        migrations.CreateModel(
            name='Salary_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_designation', models.CharField(choices=[('MANAGER', 'MANAGER'), ('CAPTAIN', 'CAPTAIN'), ('WAITER', 'WAITER'), ('HELPER', 'HELPER'), ('CLEANER', 'CLEANER'), ('WATCHMAN', 'WATCHMAN'), ('KITCHEN_SUPERVISOR', 'KITCHEN_SUPERVISOR')], default=None, max_length=100)),
                ('month', models.PositiveIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], verbose_name='Month')),
                ('year', models.PositiveIntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098)], default=2019, verbose_name='year')),
                ('Salary_recieved_date', models.DateTimeField()),
                ('Sal_status', models.CharField(choices=[('PAID', 'PAID'), ('NOTPAID', 'NOTPAID')], default=None, max_length=100)),
                ('Money_To_Give', models.FloatField(blank=True, default=0, null=True)),
                ('Money_To_Take', models.FloatField(blank=True, default=0, null=True)),
                ('Cleared_or_Notcleared', models.BooleanField()),
                ('Details', models.TextField(blank=True, max_length=1000)),
                ('created_Entry_date', models.DateTimeField(auto_now=True)),
                ('Employee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employee_App.Employee_name')),
            ],
            options={
                'verbose_name': 'Salary_Status',
                'verbose_name_plural': 'Salary_Statuses',
                'db_table': ' Salary_Status',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From_Date', models.DateField()),
                ('To_Date', models.DateField(blank=True, null=True)),
                ('no_of_Days', models.IntegerField(blank=True, editable=False, null=True)),
                ('year', models.PositiveIntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098)], default=2019, verbose_name='year')),
                ('month', models.PositiveIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], verbose_name='Month')),
                ('reason_of_leave', models.TextField(blank=True, max_length=600)),
                ('created_Entry_date', models.DateTimeField(auto_now=True)),
                ('Employee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employee_App.Employee_name')),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
                'db_table': 'Leave',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Photo', models.ImageField(blank=True, null=True, upload_to='Employee_Photos')),
                ('Employee_Mobile', models.CharField(blank=True, max_length=25, null=True)),
                ('Employee_Email', models.EmailField(blank=True, max_length=254)),
                ('Bank_Account', models.CharField(blank=True, max_length=100, null=True)),
                ('Working_or_NotWorking', models.BooleanField()),
                ('IdProof', models.ImageField(blank=True, null=True, upload_to='Employee_Id_Proofs')),
                ('Date_of_join', models.DateField()),
                ('Date_of_leave', models.DateField(blank=True, null=True)),
                ('role_designation', models.CharField(choices=[('MANAGER', 'MANAGER'), ('CAPTAIN', 'CAPTAIN'), ('WAITER', 'WAITER'), ('HELPER', 'HELPER'), ('CLEANER', 'CLEANER'), ('WATCHMAN', 'WATCHMAN'), ('KITCHEN_SUPERVISOR', 'KITCHEN_SUPERVISOR')], default=None, max_length=100)),
                ('Living_Adress', models.TextField(blank=True, max_length=600)),
                ('created_Entry_date', models.DateTimeField(auto_now=True)),
                ('Employee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employee_App.Employee_name')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': ' Employee',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Present_Absent', models.BooleanField()),
                ('Time_in', models.DateTimeField(blank=True, null=True)),
                ('Time_Out', models.DateTimeField(blank=True, null=True)),
                ('year', models.PositiveIntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098)], default=2019, verbose_name='year')),
                ('month', models.PositiveIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], verbose_name='Month')),
                ('Attnd_status', models.PositiveIntegerField(choices=[(0, 'LEAVE'), (1, 'PRESENT')], verbose_name='Attend_status')),
                ('created_Entry_date', models.DateTimeField(auto_now=True)),
                ('Employee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employee_App.Employee_name')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
                'db_table': 'Attendance',
            },
        ),
        migrations.CreateModel(
            name='Advance_amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], verbose_name='Month')),
                ('year', models.PositiveIntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098)], default=2019, verbose_name='year')),
                ('Advance_Amount_Taken', models.FloatField()),
                ('Whole_Or_Partial_Amount_Paid_in_Middle', models.FloatField(blank=True, null=True)),
                ('Advance_Taken_Date', models.DateTimeField()),
                ('Cleared_or_Notcleared', models.BooleanField()),
                ('created_Entry_date', models.DateTimeField(auto_now=True)),
                ('Employee_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employee_App.Employee_name')),
            ],
            options={
                'db_table': 'Advance_amount',
            },
        ),
    ]