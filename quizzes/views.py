from rest_framework import viewsets
from .models import Quiz
from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    """
    🪄 ModelViewSet automatically provides:
    - GET /api/v1/quizzes/ (list)
    - POST /api/v1/quizzes/ (create) 
    - GET /api/v1/quizzes/<id>/ (retrieve)
    - PUT /api/v1/quizzes/<id>/ (update)
    - PATCH /api/v1/quizzes/<id>/ (partial update)
    - DELETE /api/v1/quizzes/<id>/ (destroy)
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer