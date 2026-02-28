from django.db import models
from django.urls import reverse

class Genre(models.Model): #Should be sorted by name in ascending order
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return'{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('bookclub:bookclub', args=[str(self.name)])

class Book(models.Model): #Should be sorted by the date it was published in descending order
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name="books"
    )
    author = models.CharField()
    pubYear = models.IntegerField()
    createdOn = models.DateTimeField() #only gets set when the model is created
    updatedOn = models.DateTimeField() #always updated on the last model update