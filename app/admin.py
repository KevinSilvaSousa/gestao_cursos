from django.contrib import admin
from app.models.cursomodel import CursoModel
from app.models.usuariomodel import UsuarioModel
from app.models.matriculamodel import MatriculaModel

# Register your models here.


admin.site.register(UsuarioModel)
admin.site.register(CursoModel)
admin.site.register(MatriculaModel) 