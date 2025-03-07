from .models import Choices, Question, Quiz
from .serializers import ChoicesSerializer, QuestionSerializer, QuizSerializer
from rest_framework.views import APIView, Response
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils.dateparse import parse_datetime

def success_response(data,message="Response succesfull"):
    return Response({
        "status" : "success",
        "message" : message,
        "data" : data,
    },status=200)

def error_response(e,status=500,message="An error occured"):
    return Response({
        "status" : "error",
        "message" : message,
        "error" : str(e)
    },status=status)

def filter_quiz(search, category, difficulty, start_date, end_date):
    quizzes = Quiz.objects.all()
    # Search Filter
    if search:
        quizzes = quizzes.filter(Q(title__icontains=search) | Q(description__icontains=search))
    
    # Category Filter
    if category:
    
        quizzes = quizzes.filter(category=category)

    # Difficulty Filter
    if difficulty:
        quizzes = quizzes.filter(difficulty=difficulty)
    
    # Date Filter
    if start_date:
        start_date = parse_datetime(start_date)
    if end_date:
        end_date = parse_datetime(end_date) + timedelta(days=1)
    
   
    if start_date == None or end_date == None:
        pass
    elif start_date and end_date:
        quizzes = quizzes.filter(created_at__gte=start_date, created_at__lte=end_date)
    return quizzes

    
    


def get_questions(quiz):

    questions = Question.objects.filter(quiz=quiz["id"])
    question_serializer = QuestionSerializer(questions,many=True)
    for question in question_serializer.data:
    
        choices = Choices.objects.filter(question=question["id"])
        choices_serializer = ChoicesSerializer(choices, many=True)
        question["choices"] = choices_serializer.data
    return question_serializer.data

class QuizListCreate(APIView):



    def get(self, request):
        try:
            search = request.GET.get('search')
            category = request.GET.get('category')
            difficulty = request.GET.get('difficulty')
            start_date = request.GET.get('date_from')
            end_date = request.GET.get('date_to')
            
            quizzes = filter_quiz(search,category,difficulty,start_date,end_date)

            serialized_quiz = QuizSerializer(quizzes,many=True)
            for quiz in serialized_quiz.data:
                quiz["questions"] = get_questions(quiz)
                quiz["question_count"] = len(Question.objects.filter(quiz=quiz["id"]))

            data = {
                "quizzes" : serialized_quiz.data,
                "quiz_count" : len(quizzes)
            }
            return success_response(data,
                                    message="Quizzes retrieved successfully",)
        except Exception as e:
        
            return error_response(e)
    
    def post(self,request):
        try:
            serializer = QuizSerializer(data=request.data)
            title = request.data.get("title")
            if Quiz.objects.filter(title=title):
                return error_response(f"Quiz with title {title} already exists.", status=400 ,message="Quiz title already exists")
            if serializer.is_valid():
                serializer.save()
            return success_response(message="Quiz creation successfull",
                                    data=serializer.data)
        except Exception as e:
        
            return error_response(e)

class QuizByID(APIView):
    def get(self,request,id):
        try:
            try:
                quiz = Quiz.objects.get(pk=id)
            except Exception as e:
                return error_response(e,status=404)
            
            serializer = QuizSerializer(quiz)
            return success_response(message="Quiz retrieval successfull",data=serializer.data)
        except Exception as e:
            return error_response(e)
    
    def delete(self,request,id):
        try:
        
            quiz = Quiz.objects.get(pk=id)
            serializer = QuizSerializer(quiz)
            quiz.delete()
            return success_response(serializer.data)
        except Exception as e:
            return error_response(e)
        
    def put(self,request,id):
        try:
            data = request.data
            try:
                quiz = Quiz.objects.get(pk=id)
            except Exception as e:
                return error_response(e, status=404)
            serializer = QuizSerializer(quiz,data=data)
            if Quiz.objects.filter(title=data.get("title")) and data.get("title") != quiz.title:
                return error_response(f"Quiz with title {data.get("title")} already exists.", status=400 ,message="Quiz title already exists")
            if serializer.is_valid():
                serializer.save()
            return success_response(message="Quiz update successfull", data=serializer.data)
        except Exception as e:
            return error_response(e)

