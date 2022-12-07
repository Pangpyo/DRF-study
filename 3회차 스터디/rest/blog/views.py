# 데이터 처리
from .models import Blog, Comment, Like
from .serializer import BlogSerializer, CommentSerializer, LikeSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

# Blog의 목록
class BlogList(APIView):
    permission_classes = (IsAuthenticated,)
    # Blog list를 보여줄 때
    def get(self, request):
        blogs = Blog.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    # 새로운 Blog 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Blog의 detail
class BlogDetail(APIView):
    # Blog 객체 가져오기
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    # Blog의 detail 보기
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    # Blog 수정하기
    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 삭제하기
    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# comment의 목록을 보여주는 역할
class Commentlist(APIView):
    permissions_classes = [IsAuthenticated]

    # comment list를 보여줄 때
    def get(self, request, pk):
        comments = Comment.objects.filter(blog_id=pk)
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    # 새로운 comment를 작성할 때
    def post(self, request, pk):
        # request.data는 사용자의 입력 데이터
        serializer = CommentSerializer(data=request.data)
        blog = Blog.objects.get(pk=pk)
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.validated_data["blog"] = blog
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# comemnt의 detail을 보여주는 역할
class Commentdetail(APIView):
    # comment 객체 가져오기
    def get_object(self, request, blog_pk, comment_pk):
        try:
            return Comment.objects.get(
                blog_id = blog_pk, pk=comment_pk
            )
        except Blog.DoesNotExist:
            raise Http404

    # comment의 detail 보기
    def get(self, request, blog_pk, comment_pk, format=None):
        comment = Comment.objects.get(
            blog_id=blog_pk, pk=comment_pk
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    # 새로운 recomment를 작성할 때
    def post(self, request, blog_pk, comment_pk):
        # request.data는 사용자의 입력 데이터
        serializer = CommentSerializer(data=request.data)
        blog = Blog.objects.get(pk=blog_pk)
        comment = Comment.objects.get(pk=comment_pk)
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.validated_data["parent"] = comment
            serializer.validated_data["blog"] = blog
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # comment 수정하기
    def put(self, request, blog_pk, comment_pk, format=None):
        comment = Comment.objects.get(
            blog_id=blog_pk, pk=comment_pk
        )
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # comment 삭제하기
    def delete(self, request, blog_pk, comment_pk, format=None):
        comment = Comment.objects.get(
            blog_id=blog_pk, pk=comment_pk
        )
        if comment.user == request.user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Likelist(APIView):
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        likes = Like.objects.filter(blog=blog)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        # request.data는 사용자의 입력 데이터
        serializer = LikeSerializer(data=request.data)
        blog = Blog.objects.get(pk=pk)
        like = Like.objects.filter(blog_id=pk, user=request.user)
        if serializer.is_valid():  # 유효성 검사
            if not like:
                serializer.validated_data["user"] = request.user
                serializer.validated_data["blog"] = blog
                serializer.save()  # 저장
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                like.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)