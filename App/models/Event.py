from django.db import models


class Event(models.Model):
    e_id = models.IntegerField(primary_key=True)
    e_name = models.CharField(max_length=150)
    single = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    stage = models.IntegerField()
    node_id = models.IntegerField()
    profession = models.CharField(max_length=50)
    demand = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    mess_prize = models.CharField(max_length=500)
    mess_punishment = models.CharField(max_length=500)
    check = models.CharField(max_length=150)
    choice = models.BooleanField(default=False)
    prize = models.CharField(max_length=150)
    punishment = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.e_name

    def get_date_update(self):
        return self.date_update.strftime('%Y-%m-%d %H:%M')

    class Meta:
        app_label = 'arhem_data'
