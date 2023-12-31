from django.db import models
from django.contrib import admin

class Advertisement(models.Model):
    id = models.CharField("id", max_length=64, primary_key=True)
    title=models.CharField('заголовок', max_length=128)
    description=models.TextField('описание')
    price=models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction=models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '<Advertisement: Advertisement(id={}, title={}, price={})>.'.format(self.id, self.title, self.price)
    class Meta:
        db_table = "advertisements"
    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date()==timezone.now().date():
            created_time=self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}', created_time)
    @admin.display(description='дата создания')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date()==timezone.now().date():
            up_time=self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}', up_time)


