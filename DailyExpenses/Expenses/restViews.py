import logging

from django.db import connection
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


Logger = logging.getLogger(__name__)


class DashboardApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        # Data retrieval operation - no commit required
        cursor.execute("select strftime('%m',date) as month, sum(amount) as amount from expenses_expense  where strftime('%Y',date)=strftime('%Y') group by strftime('%m-%Y',date)")
        row = cursor.fetchall()
        Logger.error(row)
        return Response(row, status=200)

