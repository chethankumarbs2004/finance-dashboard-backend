from rest_framework.viewsets import ModelViewSet
from .models import Record
from .serializers import RecordSerializer
from users.permissions import RolePermission

class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    allowed_roles = ['ADMIN', 'ANALYST']

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        # Filtering
        type = request.GET.get('type')
        category = request.GET.get('category')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if type:
            queryset = queryset.filter(type=type)
        if category:
            queryset = queryset.filter(category=category)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset