from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Creating the Profile model. A profile is linked to a user using the user's username. 
# Contains two fields: username and image.
# Refactoring required to add more fields later.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaultt.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Triggers signal for updating profile (check signals.py file)
    def save(self,*args,**kwargs):
        super().save()

        img = Image.open(self.image.path)
        # Handles image size to fit display.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
