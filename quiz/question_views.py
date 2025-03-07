import json
from rest_framework.views import APIView, Response

from quiz.models import Choices, Question, Quiz
from quiz.serializers import ChoicesSerializer, QuestionSerializer
from quiz.views import success_response, error_response

class CreateListQuestions(APIView):
    
    def get(self,request,quizId):
        try:
            quiz = Quiz.objects.get(pk=quizId)  
            questions = Question.objects.filter(quiz=quiz)
            serializer = QuestionSerializer(questions,many=True)
            for question in serializer.data :
                choices = Choices.objects.filter(question=question["id"])
                choice_serializer = ChoicesSerializer(choices,many=True)
                question["choices"] = choice_serializer.data
            return success_response(serializer.data, message="Question retrieval successfull")
        except Quiz.DoesNotExist as e:
            return error_response(status=404,
                                  message="Corresponding Quiz not found",
                                  e=e
                                  )
        except Exception as e:
            return error_response(e=e)
    
    def post(self,request,quizId):
        try:
            quiz = Quiz.objects.get(id=quizId)
            question = request.data
            question["quiz"] = quiz.id
            choices_data = None
            if question["choices"]:
                choices_data = json.loads(question.pop("choices",None))
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                question_instance = serializer.save()
                if question.get("type") == "Multiple Choices" or question.get("type") == 'True / False' and choices_data:
                    for choice_data in choices_data:
                        Choices.objects.create(question=question_instance, choice_text=choice_data["choice_text"])
            return success_response(serializer.data, message="Question creation successfull")
        except Quiz.DoesNotExist as e:
            print(e)
            return error_response(status=404,
                                  message="Corresponding Quiz not found",
                                  e=e
                                  )
        except Exception as e:
            print(e)
            return error_response(e=e)
        

class QuestionByID(APIView):

    def delete(self,request,quiz_id,id):
        try:
            quiz = Quiz.objects.get(id=quiz_id)
            question = Question.objects.get(id=id)
            if question.quiz.id != quiz.id:
                return error_response(  
                    status=400,
                    message="Question doesn't belong to Quiz",
                    e="Bad Request"
                    )
            question.delete()
            
            
            return success_response("", message="Question deleted successfully")
        except Question.DoesNotExist as e :
            return error_response(
                status=404,
                message="Corresponding Question not found",
                e=e
            )
        except Quiz.DoesNotExist as e :
            return error_response(
                status=404,
                message="Corresponding Quiz not found",
                e=e
            )
    

    def put(self, request, quiz_id, id):
        try:
            quiz = Quiz.objects.get(id=quiz_id)
            question = Question.objects.get(id=id)
            if question.quiz.id != quiz.id:
                print("not same")
                return error_response(  
                    status=400,
                    message="Question doesn't belong to Quiz",
                    e="Bad Request"
                    )
            new_question = request.data
            choices_data = None
            if new_question["choices"]:
                choices_data = json.loads(new_question.pop("choices",None))
                print(type(choices_data))
            serializer = QuestionSerializer(question,data=request.data)
            if serializer.is_valid():
                question_instance = serializer.save()
                curr_choices = Choices.objects.filter(question=question_instance)
                for choice in curr_choices:
                    choice.delete()

                if new_question.get("type") == "Multiple Choices" or new_question.get("type") == 'True / False' and choices_data:
                    for choice_data in choices_data:
                        # print(end="")
                        Choices.objects.create(question=question_instance, choice_text=choice_data["choice_text"])
            return success_response("", message="Question deleted successfully")
        except Question.DoesNotExist as e :
            print(e)
            return error_response(
                status=404,
                message="Corresponding Question not found",
                e=e
            )
        except Quiz.DoesNotExist as e :
            print(e)
            return error_response(
                status=404,
                message="Corresponding Quiz not found",
                e=e
            )
        except Exception as e:
            print(e)
            return error_response(
                e=e
            )