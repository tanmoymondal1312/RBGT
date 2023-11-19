from django.utils import timezone
import uuid
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PictureUploadForm
from .models import UserSession, Images
from XXX.RBGT import *

def index(request):
    processed_image_url = None 

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
            image_name = original_file_name
            image_instance = Images(session=user_session, image=unique_name, image_name=image_name)
            image_instance.save()
            file_path = os.path.join('media', 'images', unique_name)
            with open(file_path, 'wb') as file:
                for chunk in form.cleaned_data['image'].chunks():
                    file.write(chunk)
            
            processed_image_path = remove_background(unique_name)
            
            existing_image_instance = Images.objects.get(image=unique_name)

            # Update the converted_image field
            existing_image_instance.converted_image = processed_image_path
            existing_image_instance.save()
            
            processed_image_url = existing_image_instance.converted_image.url

            # Store processed_image_url in the session
            request.session['processed_image_url'] = processed_image_url
    
            return redirect('index')
    else:
        form = PictureUploadForm()

    # Retrieve processed_image_url from the session
    processed_image_url = request.session.get('processed_image_url')
    request.session['processed_image_url'] = None  # Clear the session value

    print("Processed Image URL outside POST block:", processed_image_url)
            
    return render(request, 'index.html', {'form': form, 'processed_image_url': processed_image_url})
