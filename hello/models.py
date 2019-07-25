from django.db import models
from django.contrib import admin

# Create your models here.
class AppDownload(models.Model):
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	app_id = models.CharField(max_length=100)
	downloaded_at = models.DateTimeField("date downloaded")
	country = models.CharField(max_length=100, default="")

	def __str__(self):
		s = self.app_id + ' - ' + str(self.country) + ' - ' + str(self.downloaded_at.day) + '/' + str(self.downloaded_at.month) + '/' + str(self.downloaded_at.year) + ' - ' + str(self.downloaded_at.hour) + ':' + str(self.downloaded_at.minute)
		return s

admin.site.register(AppDownload)