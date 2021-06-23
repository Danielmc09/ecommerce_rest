from django.db import models
from simple_history.models import HistoricalRecords
# app_local
from apps.base.models import BaseModel
from apps.users.models import User

# Create your models here.

class Products(BaseModel):
    """Model definition for Product."""
    name = models.CharField('Nombre de Producto', max_length=150, unique = True,blank = False,null = False)
    description = models.TextField('Descripción de Producto',blank = False,null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

class Bills(BaseModel):
    """Model definition for Bills."""
    client_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Indicador de Oferta')
    company_name = models.CharField('Nombre de la Compañia',max_length=200, blank = False,null = False)
    nit = models.CharField('Nit de la Compañia',max_length=15, blank = False,null = False)
    code = models.ManyToManyField(Products)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.company_name