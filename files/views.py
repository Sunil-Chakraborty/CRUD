from django.shortcuts import render, redirect, get_object_or_404
from .models import Directory, File
from .forms import DirectoryForm, FileForm

def directory_view(request, dir_id=None):
    if dir_id:
        current_directory = get_object_or_404(Directory, id=dir_id)
        subdirectories = current_directory.subdirectories.all()
        files = current_directory.files.all()
    else:
        current_directory = None
        subdirectories = Directory.objects.filter(parent=None)
        files = File.objects.filter(directory=None)

    context = {
        'current_directory': current_directory,
        'subdirectories': subdirectories,
        'files': files,
        'dir_form': DirectoryForm(),
        'file_form': FileForm(),
    }
    return render(request, 'files/file.html', context)

def add_directory(request):
    if request.method == 'POST':
        form = DirectoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('files:home')

def add_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('files:home')

def delete_directory(request, pk):
    directory = get_object_or_404(Directory, pk=pk)
    directory.delete()
    return redirect('files:home')

def delete_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    return redirect('files:home')
