from django.db import models
import uuid
# Create your models here.
# database tables
# model forms will take the data into account "textfield" when using modelform will create the textfield etc
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    featured_image =  models.ImageField(null=True, blank=True, default="default.jpg")
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class Review(models.Model):
    VOTE_TYPE = ( #tuple to give the option to up or down vote on a particular item
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),

    )
    #foreign key 1 to many relationship
    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # CASCADE will delete all items if the project is deleted
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=2000, null=True, blank=True, choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

#many to many relationship
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name