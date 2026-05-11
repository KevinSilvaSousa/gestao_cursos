from django.db import models


class UsuarioModel(models.Model):
    """Esse é o modelo de campos do Usuario"""
    usuario = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    telefone = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(blank=False, null=False)


    def __str__(self):
        return self.usuario
        

