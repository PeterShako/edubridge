from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import FileUpload
from .forms import FileUploadForm

def upload_files(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_files')  # Reload page after upload
    else:
        form = FileUploadForm()

    files = FileUpload.objects.all()  # Retrieve all files
    return render(request, 'file_manager/upload.html', {'form': form, 'files': files})

def download_file(request, file_id):
    try:
        file = FileUpload.objects.get(id=file_id)
        response = HttpResponse(file.file, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file.name}"'
        return response
    except FileUpload.DoesNotExist:
        raise Http404

