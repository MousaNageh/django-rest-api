from django.shortcuts import render
from apiapp.models import Article
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apiapp.serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


# @csrf_exempt
# def allArticles(request):
#     # create
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         sealizer = ArticleSerializer(data=data)
#         if sealizer.is_valid():
#             sealizer.save()
#             return JsonResponse(sealizer.data, status=201)
#         return JsonResponse(sealizer.errors, status=400)

#     allArticales = ArticleSerializer(Article.objects.all(), many=True)
#     # return HttpResponse(JSONRenderer().render(allArticales.data))
#     return JsonResponse({"articales": allArticales.data})


# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return JsonResponse({"not exist": f"object of id {pk} not exists "}, status=404)

#     # update
#     if request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     # delete
#     elif request.method == "DELETE":
#         article.delete()
#         return JsonResponse({"deleted": f"aritcle of id : {pk} is deleted "}, status=204)

#     # get
#     serializer = ArticleSerializer(article)
#     return JsonResponse(serializer.data)

##########################################################################################################


# @api_view(["GET", "POST"])
# def allArticles(request):
#     # create
#     if request.method == "POST":
#         sealizer = ArticleSerializer(data=request.data)
#         if sealizer.is_valid():
#             sealizer.save()
#             return Response(sealizer.data, status=status.HTTP_201_CREATED)
#         return Response(sealizer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "GET":
#         allArticales = ArticleSerializer(Article.objects.all(), many=True)
#         # return HttpResponse(JSONRenderer().render(allArticales.data))
#         return Response(allArticales.data, status=status.HTTP_200_OK)


# @api_view(["GET", "POST", "PUT", "DELETE"])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"not exist": f"object of id {pk} not exists "}, status=status.HTTP_404_NOT_FOUND)

#     # update
#     if request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # delete
#     elif request.method == "DELETE":
#         article.delete()
#         return Response({"deleted": f"aritcle of id : {pk} is deleted "}, status=status.HTTP_204_NO_CONTENT)

#     # get
#     serializer = ArticleSerializer(article)
#     return Response(serializer.data, status=status.HTTP_200_OK)


#############################################################################################################################
class ArticleView(APIView):
    def get(self, request):
        serializer = ArticleSerializer(Article.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get_article(self, pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        selailizer = ArticleSerializer(self.get_article(pk))
        return Response(selailizer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        selailizer = ArticleSerializer(self.get_article(pk), data=request.data)
        if selailizer.is_valid():
            selailizer.save()
            return Response(selailizer.data, status=status.HTTP_200_OK)
        return Response(selailizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        serializer = self.get_article(pk)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
