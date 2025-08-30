from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Bill
from .serializers import BillItemSerializer

class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bill.objects.filter(company_owner=self.request.user)
    