from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from records.models import Record
from django.db.models import Sum, Q
from django.db.models.functions import TruncMonth
from django.views.generic import TemplateView
from users.permissions import RolePermission

class DashboardSummary(APIView):
    allowed_roles = ['ADMIN', 'ANALYST', 'VIEWER']

    def get(self, request):
        income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        category_totals = list(Record.objects.values('category').annotate(total=Sum('amount')))
        recent = list(Record.objects.order_by('-date')[:5].values('date', 'amount', 'type', 'category'))
        monthly_trends = list(Record.objects.annotate(month=TruncMonth('date'))
                              .values('month').annotate(
                                  income=Sum('amount', filter=Q(type='income')),
                                  expense=Sum('amount', filter=Q(type='expense'))
                              ).order_by('month'))

        return Response({
            "total_income": float(income),
            "total_expense": float(expense),
            "net_balance": float(income - expense),
            "category_totals": category_totals,
            "recent_activity": recent,
            "monthly_trends": monthly_trends
        })

class FrontendDashboard(TemplateView):
    template_name = 'dashboard/index.html'


