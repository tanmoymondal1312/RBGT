from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserSession, Images  # Import Images model
from .forms import PictureUploadForm  # Correct the import statement

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
            image_instance = Images(session=user_session, image=form.cleaned_data['image'])
            image_instance.save()

            return redirect('index')
    else:
        form = PictureUploadForm()

    return render(request, 'index.html', {'form': form})
