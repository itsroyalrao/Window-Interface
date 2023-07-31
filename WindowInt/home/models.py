from django.db import models

class Folder(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class FolderOne(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class FolderTwo(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class FolderThree(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class FolderFour(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title