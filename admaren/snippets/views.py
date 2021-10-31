from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters, status, serializers
from snippets import serializers as snippets_serializers
from snippets import models as snippets_models


class SnippetsViewSet(viewsets.ModelViewSet):
    serializer_class = snippets_serializers.SnippetsSerializer
    queryset = snippets_models.TextSnippet.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            serializer = snippets_serializers.SnippetsListSerializer
        else:
            serializer = snippets_serializers.SnippetsSerializer
        return serializer


class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = snippets_serializers.TagsSerializer
    queryset = snippets_models.Tag.objects.all()


class DashBoardViewSet(viewsets.ViewSet):
    def list(self, request):
        response = {}
        data_count = snippets_models.TextSnippet.objects.all()
        response['total_count'] = data_count.count()
        serializer = snippets_serializers.SnippetsListSerializer(data_count, many=True)
        response['list'] = serializer.data
        return Response(response)