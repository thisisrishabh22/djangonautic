from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  body  = models.TextField()
  slug  = models.SlugField()
  date  = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.title

  def snippet(self) -> str:
    concat = ""
    if len(self.body) > 50:
      concat = "..."
    return self.body[:50]+concat
