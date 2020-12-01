from django.db import models

class ContaCorrente(models.Model):
    numero_conta = models.CharField("Número da conta", max_length=6)
    saldo = models.DecimalField("Saldo", max_digits=20, decimal_places=2)
