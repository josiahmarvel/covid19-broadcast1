from django.db import models

from django.urls import reverse












class Speech(models.Model):
   
    title = models.CharField(max_length=200)
    speaker = models.ForeignKey('Speaker', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=None, help_text='Enter speech here')
    date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        
        return self.title

    def get_absolute_url(self):
       
        return reverse('speech-detail', args=[str(self.id)])

    




import uuid 

class SpeechInstance(models.Model):
    """Model representing a specific copy of a speech (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    speech = models.ForeignKey('Speech', on_delete=models.RESTRICT)
    

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.speech.title})'




class Speaker(models.Model):
    """Model representing a speaker."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True, max_length=2000, help_text='Enter biography here')
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular speaker instance."""
        return reverse('speaker-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'





