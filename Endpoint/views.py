from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import datetime
import pytz
from django.utils import timezone
# Create your views here.


class StageOne(APIView):
    def get(self, request):
        slack_name = request.query_params.get('slack_name','Michael')
        track = request.query_params.get('track','Backend')

        # Current Week
        current_day = datetime.datetime.now().strftime("%A")

        # Current UTC time
        current_utc_time = timezone.now()
        utc_time_format = "%Y-%m-%dT%H:%M:%SZ"

        # Github file url
        github_file_url = "https://github.com/micky225/HNG_stage_one"
        github_repo_url = "https://github.com/micky225/HNG_stage_one/blob/master/Endpoint/views.py"
    

        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_utc_time.strftime(utc_time_format),
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": status.HTTP_200_OK
        }
        return Response(response_data, status=status.HTTP_200_OK)