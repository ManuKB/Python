from django import forms


class MonthYearForm(forms.Form):
    MONTH_CHOICES = [
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
    ]
    YEAR_CHOICES = [(year, str(year)) for year in range(2000, 2051)]

    month = forms.ChoiceField(choices=MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
