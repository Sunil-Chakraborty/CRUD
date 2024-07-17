from employee.models import Employee
import django_filters
from django_filters import DateFilter

class EmployeeFilter(django_filters.FilterSet):
    start_date=DateFilter
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['eid']
