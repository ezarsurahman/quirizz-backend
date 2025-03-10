from django.shortcuts import render
from rest_framework.views import APIView, Request, Response
from quiz.views import error_response, success_response
from submission.models import Submission
from submission.serializers import SubmissionSerializer

# Create your views here.

class SubmissionListCreate(APIView):

    def post(self, request,quiz_id):
        submission_data = request.data
        submission_data["grade"] = 0
        serializer = SubmissionSerializer(data=submission_data)
        if serializer.is_valid():  
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self,request,quiz_id):
        try:
            submission = Submission.objects.get(quiz=quiz_id)
            if(submission):
                serializer = SubmissionSerializer(submission)
                return success_response(data=serializer.data)
        except Submission.DoesNotExist as e:
            return error_response(e, status=404)
