from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from tarefa.models import *
from django.contrib.auth.models import User
from tastypie.exceptions import Unauthorized

class TarefaResource(ModelResource):

    def obj_create(self, bundle, **kwargs):

        nome = bundle.data['nome']
        dataEHoraDeInicio = bundle.data['dataEHoraDeInicio']
        usuario = bundle.data['usuario'].split("/")
        projeto = bundle.data['projeto'].split("/")

        if not Tarefa.objects.filter(projeto=projeto[4]):
            cadastrar = Tarefa()
            cadastrar.nome = bundle.data['nome']
            cadastrar.dataEHoraDeInicio = bundle.data['dataEHoraDeInicio']
            cadastrar.usuario = Usuario.objects.get(pk=usuario[4])
            cadastrar.projeto = Projeto.objects.get(pk=projeto[4])
            cadastrar.save()
            bundle.obj = cadastrar
            return bundle
        else:
            raise Unauthorized('Já existe tarefa com essa pessoa');

        '''listaExiste = Tarefa.objects.filter(nome=nome, projeto=projeto[4])

        if listaExiste.count() > 0:
            raise Unauthorized('Essa Tarefa já está atribuída a um Projeto');
        else:
            cadastrar = Tarefa()
            cadastrar.nome = bundle.data['nome']
            cadastrar.dataEHoraDeInicio = bundle.data['dataEHoraDeInicio']
            cadastrar.usuario = Usuario.objects.get(pk=usuario[4])
            cadastrar.projeto = Projeto.objects.get(pk=projeto[4])
            cadastrar.save()
            bundle.obj = cadastrar
            return bundle'''

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Ops! Você não pode deletar a lista inteira')

    class Meta:
        queryset = Tarefa.objects.all()
        resource_name = 'tarefa'
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            "nome": ('exact', 'startswith')
        }
        authorization = Authorization()


class ProjetoResource(ModelResource):

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Ops! Você não pode deletar a lista inteira')

    class Meta:
        queryset = Projeto.objects.all()
        resource_name = 'projeto'
        excludes = ['password', 'is_active']
        authorization = Authorization()


class UsuarioResource(ModelResource):

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Ops! Você não pode deletar a lista inteira')

    class Meta:
        queryset = Usuario.objects.all()
        resource_name = 'usuario'
        allowed_methods = ['get', 'post', 'put', 'delete']
        excludes = ['senha']
        filtering = {
            "nome": ('exact', 'startswith')
        }
        authorization = Authorization()


class ProjetoUsuarioResource(ModelResource):

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Ops! Você não pode deletar a lista inteira')


    class Meta:
        queryset = ProjetoUsuario.objects.all()
        resource_name = 'projetousuario'
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            "nome": ('exact', 'startswith')
        }
        authorization = Authorization()
