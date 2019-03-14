from django.db import connection
from django.http import JsonResponse
from api.models import Transaction


#Functions for computing metrics by year. SQL queries reference the year portion of transaction_date and/or join_date to filter by year. JsonResponse return type.

def Revenue(request): #Revenue = sum of sales over time interval
	cursor1 = connection.cursor()
	cursor1.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2013'""")
	revenue_2013 = cursor1.fetchone()

	cursor2 = connection.cursor()
	cursor2.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2014'""")
	revenue_2014 = cursor2.fetchone()

	cursor3 = connection.cursor()
	cursor3.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2015'""")
	revenue_2015 = cursor3.fetchone()

	cursor4 = connection.cursor()
	cursor4.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2016'""")
	revenue_2016 = cursor4.fetchone()

	return JsonResponse({'revenue': {'2013': revenue_2013, '2014': revenue_2014, '2015': revenue_2015, '2016': revenue_2016 }},safe=False)


#Active users = distinct number of users who made a transaction in time interval

def ActiveUserCount(request):
	cursor1 = connection.cursor()
	cursor1.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2013'""")
	users_2013 = cursor1.fetchone()

	cursor2 = connection.cursor()
	cursor2.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2014'""")
	users_2014 = cursor2.fetchone()

	cursor3 = connection.cursor()
	cursor3.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2015'""")
	users_2015 = cursor3.fetchone()

	cursor4 = connection.cursor()
	cursor4.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2016'""")
	users_2016 = cursor4.fetchone()

	return JsonResponse({'activeusers': {'2013': users_2013, '2014': users_2014, '2015': users_2015, '2016': users_2016 }},safe=False)


#New users = users with join dates during time interval

def NewUserCount(request):
        cursor1 = connection.cursor()
        cursor1.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',join_date)='2013'""")
        newusers_2013 = cursor1.fetchone()

        cursor2 = connection.cursor()
        cursor2.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',join_date)='2014'""")
        newusers_2014 = cursor2.fetchone()

        cursor3 = connection.cursor()
        cursor3.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2015' AND strftime('%Y',join_date)='2015'""")
        newusers_2015 = cursor3.fetchone()

        cursor4 = connection.cursor()
        cursor4.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2016' AND strftime('%Y',join_date)='2016'""")
        newusers_2016 = cursor4.fetchone()

        return JsonResponse({'newusercount': {'2013': newusers_2013, '2014': newusers_2014, '2015': newusers_2015, '2016': newusers_2016 }},safe=False)


#Average revenue per active user = revenue / active users during time interval

def AverageRevenue(request):
	
	#Compute revenue

	cursor_r1 = connection.cursor()
	cursor_r1.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2013'""")
	revenue_2013 = cursor_r1.fetchone()

	cursor_r2 = connection.cursor()
	cursor_r2.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2014'""")
	revenue_2014 = cursor_r2.fetchone()

	cursor_r3 = connection.cursor()
	cursor_r3.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2015'""")
	revenue_2015 = cursor_r3.fetchone()

	cursor_r4 = connection.cursor()
	cursor_r4.execute("""SELECT sum(sales_amount) FROM Transactions WHERE strftime('%Y',transaction_date)='2016'""")
	revenue_2016 = cursor_r4.fetchone()
	
	#Compute active users
	
	cursor_a1 = connection.cursor()
	cursor_a1.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2013'""")
	users_2013 = cursor_a1.fetchone()

	cursor_a2 = connection.cursor()
	cursor_a2.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2014'""")
	users_2014 = cursor_a2.fetchone()

	cursor_a3 = connection.cursor()
	cursor_a3.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2015'""")
	users_2015 = cursor_a3.fetchone()

	cursor_a4 = connection.cursor()
	cursor_a4.execute("""SELECT COUNT (DISTINCT user) FROM Transactions WHERE strftime('%Y',transaction_date)='2016'""")
	users_2016 = cursor_a4.fetchone()

	avg_2013 = revenue_2013[0]/users_2013[0]
	avg_2014 = revenue_2014[0]/users_2014[0]
	avg_2015 = revenue_2015[0]/users_2015[0]
	avg_2016 = revenue_2016[0]/users_2016[0]

	return JsonResponse({'avrpau': {'2013': avg_2013, '2014': avg_2014, '2015': avg_2015, '2016': avg_2016 }},safe=False)
	
	