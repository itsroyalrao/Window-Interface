from django.contrib import admin
from .models import Folder, FolderOne, FolderTwo, FolderThree, FolderFour

# Register your models here.
admin.site.register(Folder);
admin.site.register(FolderOne);
admin.site.register(FolderTwo);
admin.site.register(FolderThree);
admin.site.register(FolderFour);