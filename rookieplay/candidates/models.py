from django.db import models

class Companies(models.Model):
    company_id = models.BigIntegerField(primary_key=True)
    slug = models.SlugField()
    rank = models.IntegerField()
    name = models.CharField(max_length=200)
    revenue = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    description = models.TextField()
    urls = models.URLField()
    adjectives = models.CharField(max_length=200)
    logo = models.URLField()
    image = models.URLField()

    def __str__(Self):
        return self.text

    class Meta:
        verbose_name_plural = 'companies'

class Jobs(models.Model):
    job_id = models.BigIntegerField(primary_key=True)
    slug = models.SlugField()
    company_name = models.CharFild(max_length=200)
    job_title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)
    job_location = models.CharField(max_length=200)
    job_link = models.URLField()
    job_description = models.TextField()
    company_id = models.ForeignKey('Companies', on_delete=models.CASCADE)
    pub_date = models.DateField()

    def __str__(self):
        return "{} on {}".format(
                self.job_title,
                self.pub_date.strftime('%Y-%m-%d'))
        class Meta:
            verbose_name = 'job posting'
            verbose_name_plural = 'jobs'
            ordering = ['-pub_date']


# Create your models here.
