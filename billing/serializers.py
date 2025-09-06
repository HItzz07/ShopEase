from rest_framework import serializers

from companies.models import Company
from .models import Bill, BillItem, Customer


class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
        fields = ["id", "description", "quantity", "unit_price", "line_total"]
        read_only_fields = ["line_total"]


class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True)
    class Meta:
        model = Bill
        fields = ["id", "company", "customer", "bill_number", "date", "total_amount", "status", "items"]
        read_only_fields = ["total_amount"]
    
    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        bill = Bill.objects.create(**validated_data)
        total = 0
        print(bill)
        for item in items_data:
            obj = BillItem.objects.create(bill=bill, **item)
            total +=  obj.line_total
        
        bill.total_amount = total
        bill.save()
        return bill


class CustomerSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())  
    company_name = serializers.CharField(source='company.name', read_only=True)
    class Meta:
        model = Customer
        fields = ["id", "name", "email", "phone", "address", "company_name", "company"]
        # read_only_fields = ["company"]