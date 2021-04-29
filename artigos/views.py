from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import rispy

from .models import *
from .serializers import *



class ArticleCrud(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = []
    authentication_classes = ( )

    def create(self, request):
        # ler o arquivo da request
        arq = request.FILES['file']

        #cria um arquivo temporario com os dados do arquivo
        with open('/code/temp/temp.ris', 'wb+') as destination:
            for chunk in arq.chunks():
                destination.write(chunk)

        #ler o arquivo temporario salvo acima
        with open('/code/temp/temp.ris', 'r') as bibliography_file:
            entries = rispy.load(bibliography_file)
            for entry in entries:
                #cria os objetos mapeados pela rispy
                Article.objects.create(**entry)

        #retorna mensagem de sucesso
        return Response({'message':'Articles criados com sucesso!!'})
        
