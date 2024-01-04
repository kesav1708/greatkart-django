from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
  category_name=models.CharField(max_length=100,unique=True)
  slug=models.SlugField(max_length=100,unique=True)
  description=models.TextField(max_length=300)
  category_image=models.ImageField(upload_to='photos/categories')

  class Meta:
    verbose_name='category'
    verbose_name_plural='categories'




  ## Getting the category slug
  def get_url(self):
    return reverse('product_by_category',args=[self.slug])



  def __str__(self):
    return self.category_name
  