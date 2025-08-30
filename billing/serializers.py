from rest_framework import viewsets
from .models import Bill, BillItem


class BillItemSerializer(viewsets.ModelViewSet):
    class Meta:
        model = BillItem
        fields = ["id", "description", "quantity", "unit_price", "line_total"]


class BillSerializer(viewsets.ModelViewSet):
    class Meta:
        model = Bill
        fields = ["id", "company", "customer", "bill_number", "date", "total_amount", "status", "items"]
        read_only_fields = ["total_amount"]
    
    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        bill = Bill.objects.create(**validated_data)
        total = 0

        for item in items_data:
            obj = BillItem.objects.create(bill=bill, **item)
            total +=  obj.line_total
        
        bill.total_amount = total
        bill.save()
        return bill