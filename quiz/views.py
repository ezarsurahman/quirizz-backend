from .models import Quiz
from .serializers import QuizSerializer
from rest_framework.views import APIView, Response, Request
from rest_framework.permissions import AllowAny

def success_response(data,message="Response succesfull"):
    return Response({
        "status" : "success",
        "message" : message,
        "data" : data,
    },status=200)

def error_response(e,status=500):
    return Response({
        "status" : "error",
        "message" : "An error occured",
        "error" : str(e)
    },status=status)

class QuizListCreate(APIView):
    def get(self, request):
        try:
            quizzes =  Quiz.objects.all()
            serialized_quiz = QuizSerializer(quizzes,many=True)
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
                return error_response(f"Quiz with title {title} already exists.", status=400)
            if serializer.is_valid():
                serializer.save()
            return success_response(message="Quiz creation successfull",
                                    data=serializer.data)
        except Exception as e:
            return error_response(e)
        
class QuizDelete(APIView):
    def delete(self,request,id):
        try:
            print(id)
            quiz = Quiz.objects.get(pk=id)
            serializer = QuizSerializer(quiz)
            quiz.delete()
            return success_response(serializer.data)
        except Exception as e:
            return error_response(e)

class QuizUpdate(APIView):
    def put(self,request,id):
        try:
            data = request.data
            try:
                quiz = Quiz.objects.get(pk=id)
            except Exception as e:
                print("gajelas")
                return error_response(e, status=404)
            serializer = QuizSerializer(quiz,data=data)
            if serializer.is_valid():
                serializer.save()
            return success_response(message="Quiz update successfull", data=serializer.data)
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

