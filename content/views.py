from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed
from rest_framework.response import Response
from user.models import User
from rest_framework.response import Response
import os
from insta_clone.settings import MEDIA_ROOT
from uuid import uuid4
from datetime import datetime

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')
        email = request.data.get('email')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, email=email, like_count=0)
        
        return Response(status=200)

