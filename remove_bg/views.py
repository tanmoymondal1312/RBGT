from django.utils import timezone
import uuid
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PictureUploadForm
from .models import UserSession, Images
from XXX.RBGT import *


# ... (other imports)

def index(request):
    if not request.session.session_key:
        print("Dhukce")
        request.session.create()
        print(request.session.session_key)
        UserSession.objects.create(session_key=request.session.session_key)

    if request.method == 'POST':
        form = PictureUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_session = UserSession.objects.get(session_key=request.session.session_key)

            original_file_name, file_extension = os.path.splitext(form.cleaned_data['image'].name)
            unique_name = f"{str(uuid.uuid4())[:8]}{file_extension}"

            # Save the original file name in the 'image_name' attribute
            image_name = original_file_name

            # Create a new Images instance with the unique name and original file name
            image_instance = Images(session=user_session, image=unique_name, image_name=image_name)

            # Save the image instance
            image_instance.save()

            # Save the uploaded file with the unique name
            file_path = os.path.join('media', 'images', unique_name)
            with open(file_path, 'wb') as file:
                for chunk in form.cleaned_data['image'].chunks():
                    file.write(chunk)
            
            remove_background(unique_name)     

            return redirect('index')
    else:
        form = PictureUploadForm()

    return render(request, 'index.html', {'form': form})
