from django.db import models

# Create your models here.
class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    tittle=models.CharField(max_length=200)
    Intro=models.CharField(max_length=1000)
    head1=models.CharField(max_length=500)
    Chead1=models.CharField(max_length=2000)
    head2=models.CharField(max_length=500)
    Chead2=models.CharField(max_length=2000)
    head3=models.CharField(max_length=500)
    Chead3=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='Blog/Image',default="")
    p_date=models.DateTimeField()
    def __str__(self):
        return self.tittle