from django.db import models

class Parada(models.Model):

    name = models.CharField(("Parada"), max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        db_table = 'parada'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Linha(models.Model):

    name = models.CharField(("Linha"), max_length=50)
    paradas = models.ManyToManyField(Parada)

    class Meta:
        db_table = 'linha'
        ordering = ['name']

    def __str__(self):
        return self.name

class Veiculo(models.Model):

    name = models.CharField(("Veiculo"), max_length=50)
    model = models.CharField(("modelo"), max_length=50)
    linha = models.ForeignKey(Linha, verbose_name=(""), on_delete=models.CASCADE)

    class Meta:
        db_table = 'veiculo'
        ordering = ['name']

    def __str__(self):
        return self.name

class PosicaoVeiculo(models.Model):

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    veiculo = models.ForeignKey(Veiculo, verbose_name=(""), on_delete=models.CASCADE)

    class Meta:
        db_table = 'PosicaoVeiculo'

    def __str__(self):
        return self.veiculo