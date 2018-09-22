from django.db import models

class Browsers(models.Model):
    browsers = (
        ('Chrome', 'Chrome'),
        ('Safari', 'Safari'),
        ('Firefox', 'Firefox'),
        ('Opera', 'Opera'),
        ('Edge', 'Edge'),
        ('Others','Others'),
    )
    browsers_names = models.CharField(choices=browsers, default='Chrome', max_length=15,name='Browsers')
    browser_users = models.IntegerField(name='Users')