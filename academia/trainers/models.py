from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='trainers/', null=True, blank=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
