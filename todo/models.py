from django.db import models

class todoModels(models.Model):
    judulTodo = models.CharField(max_length = 255 )

    def __str__(self):
        return "{}. {}".format(self.id, self.judulTodo)
