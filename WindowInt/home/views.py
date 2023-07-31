from django.shortcuts import render, redirect
from .models import Folder, FolderOne, FolderTwo, FolderThree, FolderFour

# Create your views here.
def homepage(request):
  folder = Folder.objects.all()
  if request.method == 'POST':
    new_folder = Folder(
      title = request.POST['title']
    )
    if request.POST['title'] != '':
      new_folder.save()

    return redirect('/')
  
  return render(request, 'home/homepage.html', {'folders': folder})

def innerone(request):
  folder = FolderOne.objects.all()
  if request.method == 'POST':
    new_folder = FolderOne(
      title = request.POST['title']
    )
    if request.POST['title'] != '':
      new_folder.save()

    return redirect('/innerone')
  
  return render(request, 'home/innerone.html', {'folders': folder})

def innertwo(request):
  folder = FolderTwo.objects.all()
  if request.method == 'POST':
    new_folder = FolderTwo(
      title = request.POST['title']
    )
    if request.POST['title'] != '':
      new_folder.save()

    return redirect('/innertwo')
  
  return render(request, 'home/innertwo.html', {'folders': folder})

def innerthree(request):
  folder = FolderThree.objects.all()
  if request.method == 'POST':
    new_folder = FolderThree(
      title = request.POST['title']
    )
    if request.POST['title'] != '':
      new_folder.save()

    return redirect('/innerthree')
  
  return render(request, 'home/innerthree.html', {'folders': folder})

def innerfour(request):
  folder = FolderFour.objects.all()
  if request.method == 'POST':
    new_folder = FolderFour(
      title = request.POST['title']
    )
    if request.POST['title'] != '':
      new_folder.save()

    return redirect('/innerfour')
  
  return render(request, 'home/innerfour.html', {'folders': folder})


def delete(request, fol):
  folder = Folder.objects.get(id=fol)
  folder.delete()
  return redirect('/')

def deleteone(request, fol1):
  folder = FolderOne.objects.get(id=fol1)
  folder.delete()
  return redirect('/innerone')

def deletetwo(request, fol2):
  folder = FolderTwo.objects.get(id=fol2)
  folder.delete()
  return redirect('/innertwo')

def deletethree(request, fol3):
  folder = FolderThree.objects.get(id=fol3)
  folder.delete()
  return redirect('/innerthree')

def deletefour(request, fol4):
  folder = FolderFour.objects.get(id=fol4)
  folder.delete()
  return redirect('/innerfour')