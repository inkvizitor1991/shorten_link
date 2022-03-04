from django.db import models
from django.db.models import Q



class LinkQuerySet(models.QuerySet):

    def find_url(self, url):
        return self.filter(Q(received_url__icontains=url))


class Link(models.Model):
    received_url = models.URLField(
        'Полученная ссылка', unique=True, max_length=200
    )
    short_url = models.URLField(
        'Новая ссылка', unique=True, max_length=100
    )
    created_at = models.DateTimeField(
        'Когда создана новая ссылка', auto_now_add=True
    )
    amount_clicks = models.IntegerField(
        'Количество переходов по новой ссылки', default=0
    )
    objects = LinkQuerySet.as_manager()



