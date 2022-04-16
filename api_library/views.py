from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Books
from .serializers import BooksSerializer
from rest_framework.permissions import IsAuthenticated  # <-- Here


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Books.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.request.data
        try:
            book_obj = Books.objects.create(book_title=data.get('book_title'),
                                            book_author=data.get('book_author'))
            book_obj.save()
        except Exception as e:
            content = {'Error': str(e)}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        return super(BooksViewSet, self).update(request, pk=None)

    def partial_update(self, request, pk=None):
        return super(BooksViewSet, self).update(request, pk=None)

    def destroy(self, request, pk):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
