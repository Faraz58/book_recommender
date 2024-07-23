from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book, Review, User
from .serializers import BookSerializer, ReviewSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.db.models import Avg


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        genre = self.request.query_params.get('genre', None)
        if genre:
            return Book.objects.filter(genre=genre)
        return super().get_queryset()


class AddReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class UpdateReviewView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class DeleteReviewView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class SuggestBooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        reviews = Review.objects.filter(user=user)
        if not reviews.exists():
            return Response({'message': 'There is not enough data about you'}, status=status.HTTP_404_NOT_FOUND)

        favorite_genre = reviews.values('book__genre').annotate(average_rating=Avg('rating')).order_by(
            '-average_rating').first()
        if favorite_genre:
            suggestions = Book.objects.filter(genre=favorite_genre['book__genre']).exclude(review__user=user)
            serializer = BookSerializer(suggestions, many=True)
            return Response(serializer.data)

        return Response({'message': 'There is not enough data about you'}, status=status.HTTP_404_NOT_FOUND)