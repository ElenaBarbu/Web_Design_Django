from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/Images/Home/')
    paragraph = models.TextField()
    category = models.CharField(max_length=200,default="Blood Pressure")

class Review(models.Model):
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # pentru a putea modifica reviw-ul
    def update_review(self, email, rating, comment):
        self.email = email
        self.rating = rating
        self.comment = comment
        self.save()

    # pentru a putea sterge
    def delete_review(self):
        self.delete()
