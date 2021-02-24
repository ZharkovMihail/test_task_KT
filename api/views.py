from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
import os
from pathlib import Path

from .models import Picture, Tag
from .serializers import TagSerializer, PictureSerializer


@api_view(['GET', 'POST'])
def images1(request):
    """
        GET: get all images and their tags
        POST: post image and tags
            body:
                upload:  image.jpg
                tags:    tag1, tag2, tag3 ...
    """
    if request.method == 'GET':
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(dict(request.data))
        d = dict(request.data)
        picture = d["upload"][0]
        p = Picture(upload=picture)
        p.save()
        for tag in d["tags"][0].split(","):
            t, created = Tag.objects.get_or_create(
                title=tag.strip(),
            )
            p.tags.add(t)
        print(Tag.objects.values())
        return HttpResponse("Question created", status=201)


@api_view(['GET', 'DELETE', 'PATCH'])
def get_image(request, file_name):
    """
        url: media/uploads/[str:file_name]

        GET: get picture
        DELETE: delete picture from database and from dir media
        PATCH: change picture`s tags to new
            body:
                tags:   new_tag1, new_tag2, new_tag3 ...
    """
    if request.method == 'GET':
        image = Image.open('media/uploads/'+str(file_name))
        response = HttpResponse(content_type="image/jpeg")
        image.save(response, "JPEG")
        return response
    elif request.method == "DELETE":
        p = get_object_or_404(Picture, upload='uploads/'+str(file_name))
        p.delete()
        path = os.path.join((Path(__file__).resolve().parent.parent), 'media/uploads/'+str(file_name))
        os.remove(path)
        return Response("Picture deleted", status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        p = get_object_or_404(Picture, upload='uploads/'+str(file_name))
        p.tags.clear()
        d = dict(request.data)
        for tag in d["tags"][0].split(","):
            t, created = Tag.objects.get_or_create(
                title=tag.strip(),
            )
            p.tags.add(t)
        return HttpResponse("Tags updated", status=201)


@api_view(['GET'])
def get_images_by_tag(request):
    """
        url: api/images_by_tags

        GET: get images by tags
            body:
                tags:  tag1, tag2, tag3 ...
    """
    if request.method == 'GET':
        tags = request.data["tags"].split(",")
        queryset = Picture.objects.all()
        if tags != ['']:
            for item in tags:
                queryset = queryset.filter(tags__title=item.strip())
        serializer = PictureSerializer(queryset, many=True)
        return Response(serializer.data)




