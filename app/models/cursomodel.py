from django.db import models
from django.core.validators import MinLengthValidator

class CursoModel(models.Model):
    """Esse é o modelo de campos do Curso"""

    NIVEL = (
        ('B', 'Basico'),
        ('I', 'intermediario'),
        ('A', 'Avançado')
    )

    codigo = models.CharField(max_length=100, validators=[MinLengthValidator])
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, default='B', blank=False, null=True)

    def __str__(self):
        return  self.codigo


