from django.db import models
from django.contrib.postgres.fields import ArrayField


class Location(models.Model):
    node_id = models.IntegerField(primary_key=True)
    name_node = models.CharField(max_length=50)
    declension = models.CharField(max_length=50)
    contact_list_id = ArrayField(models.IntegerField())
    district = models.CharField(max_length=50)
    district_id = models.IntegerField()
    street = models.BooleanField(default=False)
    dist = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_node

    def get_date_update(self):
        return self.date_update.strftime('%Y-%m-%d %H:%M')

    class Meta:
        app_label = 'arhem_data'
