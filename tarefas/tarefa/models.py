from django.db import models
from django.utils import timezone

class Tarefa(models.Model):
    nome = models.CharField('Nome', max_length=200)
    dataEHoraDeInicio = models.DateTimeField('Data', default=timezone.now)
    usuario = models.ForeignKey('Usuario')
    projeto = models.ForeignKey('Projeto')

    def __str__(self):
        return '{}'.format(self.nome)


class Projeto(models.Model):
    nome = models.CharField('Nome', max_length=200)

    def __str__(self):
        return '{}'.format(self.nome)


class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.CharField('E-mail', max_length=200)
    senha = models.CharField('Senha', max_length=200)

    def __str__(self):
        return '{}'.format(self.nome)


class ProjetoUsuario(models.Model):
    projeto = models.ForeignKey('Projeto')
    usuario = models.ForeignKey('Usuario')

    def __str__(self):
        return '{}'.format(self.Projeto)
