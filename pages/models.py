from django.db import models



class MainScrollMode(models.Model):
    image = models.ImageField(upload_to='main-scroll')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=250)
    discount = models.PositiveSmallIntegerField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'scroll'
        verbose_name_plural = 'scrolls' 

class MainMenuMode(models.Model):
    image = models.ImageField(upload_to='main-scroll')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=250)
    discount = models.PositiveSmallIntegerField()
    price = models.IntegerField(default=0)


    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods' 