from rest_framework import serializers
from .models import TableRows


class TableRowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableRows
        fields = '__all__'
