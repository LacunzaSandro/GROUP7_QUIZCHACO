from django.db import models

class TimeModel(models.Model):
	creado = models.DateTimeField(auto_now_add=True,
								  verbose_name=u'creado',
								  help_text=u'Fecha de creación')
	modificado = models.DataTimeField(auto_now=True,
									  nerbose_name=u'modificado',
									  help_text=u'Fecha de modificación')

	class Meta:
		abstract = True