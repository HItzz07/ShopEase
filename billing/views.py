from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Bill, Customer
from .serializers import BillSerializer, CustomerSerializer

class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bill.objects.filter(company__owner=self.request.user, company__name=self.request.query_params.get("company_name"))
    
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(company__owner=self.request.user, company__name=self.request.query_params.get("company_name"))