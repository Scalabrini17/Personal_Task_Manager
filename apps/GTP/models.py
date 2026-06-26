from django.db import models

class Prioridade(models.TextChoices):
      URGENTE =   'urgente', 'Urgente'
      ALTA = 'alta', 'Alta'
      MEDIA = 'media', 'Média'
      BAIXA = 'baixa', 'Baixa'

class Status(models.TextChoices):
      EM_ESPERA =  'em_espera', 'Em Espera'
      INICIADO = 'iniciado', 'Iniciado'
      FINALIZADO = 'finalizado', 'Finalizado'

class Localizacao(models.TextChoices):
      ATIVA = 'ativa', 'Ativa'
      LIXEIRA = 'lixeira', 'Lixeira'

class Task(models.Model):
      nome = models.CharField(max_length = 50, )
      descricao = models.TextField()
      prazo = models.DateField()
      prioridade = models.CharField(max_length = 20, choices = Prioridade.choices, default = Prioridade.MEDIA)
      status = models.CharField(max_length = 20, choices = Status.choices, default = Status.EM_ESPERA)
      localizacao = models.CharField(max_length = 20, choices = Localizacao.choices, default = Localizacao.ATIVA)
    
      def __str__(self):
            return self.nome