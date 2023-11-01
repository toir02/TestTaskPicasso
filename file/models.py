from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время загрузки')
    processed = models.BooleanField(default=False, verbose_name='признак обработки')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
