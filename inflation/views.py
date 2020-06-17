from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt


def Home(request):
    # df = pd.read_csv('static/india-cpi.csv')
    # context = {
    #     'df': df.to_html(),
    #     'head': df.head().to_html(),
    # }
    # return render(request, 'inflation/index.html', context)
    return render(request, 'inflation/index.html')


def graph(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    amount = request.POST.get('amount')

    principal_amt = float(amount)

    start_date = start_date + "-12-" + "31"
    end_date = end_date + "-12-" + "31"
    final_amount = 0

    df = pd.read_csv('static/india-cpi.csv')
    df = df.set_index("date")

    inflation_list = list(df.loc[start_date:end_date, " inflation-rate"])
    print(inflation_list)

    list_for_p = []
    for item in inflation_list:
        principal_amt += principal_amt*(item/100)
        list_for_p.append(principal_amt)

    final_amount += principal_amt

    context = {
        'start_date': start_date,
        'end_date': end_date,
        'amount': amount,
        'final_amount': final_amount,
        'yearly_list' : list_for_p,
    }
    print(start_date, end_date)
    return render(request, 'inflation/graph.html', context)
