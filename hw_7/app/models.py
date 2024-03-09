from django.db  import models

# Create your models here.
class Todo(models.Model):
    class Status(models.TextChoices):
        done='d','done',
        in_progress='p','in_progress'
        not_started='n','not_started'
        achived='a','achived'
        
    title=models.CharField(max_length=255)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.done)
    description=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="ToDo"
        verbose_name_plural="ToDos"


