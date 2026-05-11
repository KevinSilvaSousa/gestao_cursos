from django.db import models
from app.models.usuariomodel import UsuarioModel
from app.models.cursomodel import CursoModel

class MatriculaModel(models.Model):
    """Esse é o modelo de campos do Matricula do Usuario"""

    PERIODO = (
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno"),
    )

    estudante = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    curso = models.ForeignKey(CursoModel, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, default="B", blank=False, null=True)

    def __str__(self):
        return self.periodo