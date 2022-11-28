from django.db import models


class Faq(models.Model):
    """
    A model class to hold the current FAQs
    """
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    title = models.CharField(max_length=100)
    friendly_title = models.CharField(max_length=100)
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
