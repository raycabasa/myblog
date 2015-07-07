from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 30)
    date = models.DateField()
    body = models.TextField()

    def __unicode__(self):
        return u'%s %s %s %s' % (self.title, self.author, self.date, self.body)

