from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True) #최초추가
  updated_at = models.DateTimeField(auto_now=True) #수정될때마다
  image = models.ImageField(upload_to="images/", blank=True)
  
  def __str__(self):
        return self.title

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
  content = models.CharField(max_length=120)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.content
