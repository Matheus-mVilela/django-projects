from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__ (self):
        return self.num_doc

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to="clientes_photos", null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Produto(models.Model):
    preco = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
   
    def __str__ (self):
        return self.descricao



class Venda(models.Model):
    numero = models.CharField(max_length=7)
    desconto = models.DecimalField(max_digits=6, decimal_places=2)
    impostos = models.DecimalField(max_digits=6, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __srt__ (self):
        return self.numero 