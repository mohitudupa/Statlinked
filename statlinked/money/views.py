from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
import datetime


month_object = {1: JanBill, 2: FebBill, 3: MarBill, 4: AprBill, 5: MayBill, 6: JunBill, 7: JulBill, 8: AugBill,
                9: SepBill, 10: OctBill, 11: NovBill, 12: DecBill, }


month_name = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December', }


def add(bill, y, z):
    x = bill.amount * z
    if bill.tag == 'misc':
        y.m_misc += x
    if bill.tag == 'food':
        y.m_food += x
    if bill.tag == 'utilities':
        y.m_utilities += x
    if bill.tag == 'transport':
        y.m_transport += x
    if bill.tag == 'taxes':
        y.m_taxes += x
    if bill.tag == 'clothing':
        y.m_clothing += x
    if bill.tag == 'medical':
        y.m_medical += x
    if bill.tag == 'repairs':
        y.m_repairs += x
    day = bill.written_date.day
    if day < 5:
        y.spent_5 += x
    if (day >= 5) and (day < 10):
        y.spent_10 += x
    if (day >= 10) and (day < 15):
        y.spent_15 += x
    if (day >= 15) and (day < 20):
        y.spent_20 += x
    if (day >= 20) and (day < 25):
        y.spent_25 += x
    if (day >= 25) and (day < 30):
        y.spent_30 += x

    y.save()

    return


def delete_all(x):
    for i in x:
        i.delete()
    return


def reset_all(y):
    y.m_misc = 0
    y.m_food = 0
    y.m_utilities = 0
    y.m_transport = 0
    y.m_taxes = 0
    y.m_clothing = 0
    y.m_medical = 0
    y.m_repairs = 0
    y.spent_5 = 0
    y.spent_10 = 0
    y.spent_15 = 0
    y.spent_20 = 0
    y.spent_25 = 0
    y.spent_30 = 0
    y.save()
    return


def recompute(x):
    chart1 = {'misc': 0, 'food': 0, 'utilities': 0, 'transport': 0, 'taxes': 0, 'clothing': 0, 'medical': 0,
              'repairs': 0}
    chart2 = [0, 0, 0, 0, 0, 0]
    for i in x:
        chart1[i.tag] += i.amount
        day = i.written_date.day
        if day < 5:
            chart2[0] += i.amount
        if (day >= 5) and (day < 10):
            chart2[1] += i.amount
        if (day >= 10) and (day < 15):
            chart2[2] += i.amount
        if (day >= 15) and (day < 20):
            chart2[3] += i.amount
        if (day >= 20) and (day < 25):
            chart2[4] += i.amount
        if (day >= 25) and (day < 30):
            chart2[5] += i.amount
    return chart1, chart2


def index(request):
    if request.user.is_authenticated:
        bills = month_object[datetime.datetime.now().month].objects.filter(user_id=request.user)[::-1]
        stats = UserData.objects.get(user_id=request.user)
        reset = False
        if stats.t_date.month != datetime.datetime.now().month or stats.t_date.year != datetime.datetime.now().year:
            delete_all(bills)
            stats.t_date = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, 1)
            reset_all(stats)
            reset = True
        return render(request, 'money/home.html', {'bills': bills, 'stats': stats, 'reset': reset})
    else:
        return redirect('home:user_login')


def add_bill(request):
    if request.user.is_authenticated and request.method == 'POST':
        x = dict(request.POST)
        bill_class = month_object[datetime.datetime.now().month]
        bill = bill_class()
        bill.user_id = request.user
        bill.tag = x['tag'][0][:25]
        bill.description = x['description'][0][:250]
        bill.amount = float(x['amount'][0])
        dattim = datetime.datetime.now()
        bill.written_date = datetime.date(dattim.year, dattim.month, dattim.day)
        bill.save()

        y = UserData.objects.get(user_id=request.user)
        if y.t_date.month != dattim.month:
            reset_all(y)
        y.t_date = bill.written_date

        add(bill, y, 1)

        return redirect('money:index')
    return redirect('money:index')


def del_bill(request):
    if request.user.is_authenticated and request.method == 'POST':
        x = dict(request.POST)
        bill_id = int(x['action'][0]) - 1
        bill_class = month_object[datetime.datetime.now().month]
        bill = bill_class.objects.filter(user_id=request.user)[::-1][bill_id]
        y = UserData.objects.get(user_id=request.user)

        add(bill, y, -1)

        bill.delete()

        return redirect('money:index')
    return redirect('money:index')


def edit_bill(request):
    if request.user.is_authenticated and request.method == 'POST':
        x = dict(request.POST)
        bill_id = int(x['action'][0]) - 1
        bill_class = month_object[datetime.datetime.now().month]
        cur_user = User.objects.get(id=request.user.id)
        bill = bill_class.objects.filter(user_id=request.user)[::-1][bill_id]
        old_date = bill.written_date
        y = UserData.objects.get(user_id=request.user)

        add(bill, y, -1)

        bill.delete()

        bill = bill_class()
        bill.user_id = cur_user
        bill.tag = x['tag'][0][:25]
        bill.description = x['description'][0][:250]
        bill.amount = float(x['amount'][0])
        bill.written_date = old_date
        bill.save()
        y.t_date = bill.written_date

        add(bill, y, 1)

        return redirect('money:index')
    return redirect('money:index')


def history(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            x = dict(request.POST)
            month = int(x['month'][0])
        else:
            month = (datetime.datetime.now().month - 1) % 12
        bills = month_object[month].objects.filter(user_id=request.user)[::-1]
        chart1, chart2 = recompute(bills)
        year = datetime.datetime.now().year
        if int(month) > datetime.datetime.now().month:
            year -= 1
        return render(request, 'money/history.html',
                      {'bills': bills, 'month': month_name[month], 'year': year, 'misc': chart1['misc'],
                       'food': chart1['food'], 'utilities': chart1['utilities'], 'transport': chart1['transport'],
                       'taxes': chart1['taxes'], 'clothing': chart1['clothing'], 'medical': chart1['medical'],
                       'repairs': chart1['repairs'], 'day5': chart2[0], 'day10': chart2[1], 'day15': chart2[2],
                       'day20': chart2[3], 'day25': chart2[4], 'day30': chart2[5]})
    else:
        return redirect('home:user_login')


def update_goal(request):
    if request.user.is_authenticated and request.method == 'POST':
        x = dict(request.POST)
        dattim = datetime.datetime.now()
        y = UserData.objects.get(user_id=request.user)
        if len(x) == 4:
            bills = month_object[dattim.month].objects.filter(user_id=request.user)[::-1]
            delete_all(bills)
            y.t_date = datetime.date(dattim.year, dattim.month, dattim.day)
            reset_all(y)
        y.goal = float(x['goal'][0])
        y.save()
    return redirect('money:index')
