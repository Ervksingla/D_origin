from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Content
from .serializers import ContentSerializer

class ContentView(APIView):
    def get(self, request):
        contents = Content.objects.filter(is_deleted=False)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContentDetailView(APIView):
    def get(self, request, pk):
        try:
            content = Content.objects.get(pk=pk, is_deleted=False)
        except Content.DoesNotExist:
            return Response({"error": "Content not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContentSerializer(content)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            content = Content.objects.get(pk=pk, is_deleted=False)
        except Content.DoesNotExist:
            return Response({"error": "Content not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            content = Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            return Response({"error": "Content not found"}, status=status.HTTP_404_NOT_FOUND)

        content.is_deleted = True
        content.save()
        return Response({"message": "Content deleted"}, status=status.HTTP_204_NO_CONTENT)