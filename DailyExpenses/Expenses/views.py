import logging

import django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from django.db.models import Sum
from django.forms import DateInput, forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Expense

Logger = logging.getLogger(__name__)

def resume(request):
    return render(request, 'resume.html', {})


@login_required(login_url='/login')
def deleteAll(request):
    Expense.objects.all().delete()
    expenses = Expense.objects.all()
    total = Expense.objects.aggregate(Sum('amount'))
    context = {
        'expenses': expenses,
        'total': total,
    }
    return render(request, 'home.html', context)


def savings(request):
    return render(request, 'Saving.html', {})


def birthday(request):
    return render(request, 'hbd.html', {})


@login_required(login_url='/login')
def dashboard(request):
    expenses = Expense.objects.all()
    total = Expense.objects.aggregate(Sum('amount'))
    context = {
        'expenses': expenses,
        'total': total,
    }
    cursor = connection.cursor()

    # Data retrieval operation - no commit required
    cursor.execute("select strftime('%m',date), sum(amount) from expenses_expense group by strftime('%m-%Y',date)")
    row = cursor.fetchall()
    Logger.error(row)
    return render(request, 'dashboard.html', context)


month = django.utils.timezone.now().month
month= "{:02d}".format(month)
year = django.utils.timezone.now().year
day = django.utils.timezone.now().day
day= "{:02d}".format(day)


class ExpenseListView(ListView):
    model = Expense
    template_name = 'home.html'
    context_object_name = 'expenses'
    ordering = ['-date']
    paginate_by = 20

    def get_context_data(self, **kwargs):
        filter_from = self.request.GET.get('filter_from', '')
        filter_to = self.request.GET.get('filter_to', '')
        total = Expense.objects.filter(date__month=month, date__year=year).aggregate(Sum('amount')) if filter_from =="" else  Expense.objects.filter(date__range=[filter_from, filter_to]).aggregate(Sum('amount'))
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        context['total'] = total
        # context['u_form'] = MonthYearForm()
        context['filter_from'] = self.request.GET.get('filter_from', str(year)+"-"+str(month)+"-"+str(day))
        context['filter_to'] = self.request.GET.get('filter_to', str(year)+"-"+str(month)+"-"+str(day))
        return context

    def get_queryset(self):
        filter_from = self.request.GET.get('filter_from', '')
        filter_to = self.request.GET.get('filter_to', '')
        queryset = super().get_queryset()
        results = queryset.filter(date__month=month, date__year=year) if filter_from =="" else  queryset.filter(date__range=[filter_from, filter_to])
        return results

    def get_form(self):
        form = super().get_form()
        form.fields['filter_from'].widget = DateInput(attrs={'type': 'date'})
        form.fields['filter_to'].widget = DateInput(attrs={'type': 'date'})
        return form


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    success_url = '/home'
    template_name = 'createExpense.html'
    fields = ['name', 'amount', 'date']

    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = 'createExpense.html'
    success_url = '/home'
    fields = ['name', 'amount', "date"]

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = DateInput(attrs={'type': 'date'})
        return form

    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.added_by:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(ExpenseUpdateView, self).get_context_data(**kwargs)
        context['type'] = "update"
        return context


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = '/home'
    template_name = 'deleteConfirm.html'

    def test_func(self):
        expense = self.get_object()
        if self.request.user == expense.added_by:
            return True
        return False
