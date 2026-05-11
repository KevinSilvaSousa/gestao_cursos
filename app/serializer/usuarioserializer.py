from rest_framework import serializers
from app.models.cursomodel import CursoModel
from app.models.usuariomodel import UsuarioModel
from app.models.matriculamodel import MatriculaModel
from app.validators import validacao_cpf, nome_invalido, celular_invalido


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__'


    def validate_cpf(self, dados):
        if validacao_cpf(dados['cpf']):
            raise serializers.ValidationError ({"cpf": "O CPF deve ter 11 digitos"})
        

        if nome_invalido(dados['usuario']):
            raise serializers.ValidationError ({"nome" : "Confirme corretamente o seu nome!"})
        

        if celular_invalido(dados['telefone']):
            raise serializers.ValidationError ({"telefone" : "Formato incorreto do telefone"})
        
        