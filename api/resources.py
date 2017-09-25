# api/resources.py
from tastypie.resources import ModelResource
from api.models import Employee
from tastypie.authorization import Authorization
class EmployeeResource(ModelResource):
    class Meta:
        authorization = Authorization() # insecure as all heck
        queryset = Employee.objects.all()
        resource_name = 'employee'
        fields = ['dept', 'last_name', 'first_name', 'created_at', 'unique_id']