from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class JanBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class FebBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class MarBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class AprBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class MayBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class JunBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class JulBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class AugBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class SepBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class OctBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class NovBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag)


class DecBill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    written_date = models.DateField()

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.tag) + ' - ' + str(self.amount)


class UserData(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.FloatField(default=0)

    m_misc = models.FloatField(default=0)
    m_food = models.FloatField(default=0)
    m_utilities = models.FloatField(default=0)
    m_transport = models.FloatField(default=0)
    m_taxes = models.FloatField(default=0)
    m_clothing = models.FloatField(default=0)
    m_medical = models.FloatField(default=0)
    m_repairs = models.FloatField(default=0)

    t_misc = models.FloatField(default=0)
    t_food = models.FloatField(default=0)
    t_utilities = models.FloatField(default=0)
    t_transport = models.FloatField(default=0)
    t_taxes = models.FloatField(default=0)
    t_clothing = models.FloatField(default=0)
    t_medical = models.FloatField(default=0)
    t_repairs = models.FloatField(default=0)

    t_date = models.DateField()

    spent_5 = models.FloatField(default=0)
    spent_10 = models.FloatField(default=0)
    spent_15 = models.FloatField(default=0)
    spent_20 = models.FloatField(default=0)
    spent_25 = models.FloatField(default=0)
    spent_30 = models.FloatField(default=0)

    def __str__(self):
        return str(self.user_id.username) + ' - ' + str(self.goal)
