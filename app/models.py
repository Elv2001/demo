from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.forms import ValidationError
from datetime import datetime


class User(AbstractUser):
    FIO = models.CharField( verbose_name='ФИО', max_length=150, null=False, blank=False,
        validators=[
            RegexValidator(
                regex=r"^[а-яА-Я- ]+$",
                message=" Разрешены только кирилица , пробел или тире"
            )
        ])

    phone = models.CharField(
       verbose_name= "Телефон", max_length=30, null=False, blank=False,
        validators=[
            RegexValidator(
                regex=r"\+7\(\d\d\d\)-\d\d\d-\d\d-\d\d",
                message="Введите телефон в формате +7(XXX)-XXX-XX-XX",
                code="invalid_phone_number",
            ),
        ],
    )
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    REQUIRED_FIELDS = ["FIO",  "phone", "email"]



def statement_date_time_only_hours(value:datetime):
    if value.minute or value.second or value.microsecond:
        raise ValidationError("Разрешается запись только по часам")

class Statement(models.Model):
    class Status(models.TextChoices):
        NEW = "N", _("Новое")
        PODTV = "P", _("Подтверждено")
        OTCLON = "O", _("Отклонено")

    number = models.CharField(verbose_name="Государственный регистрационный номер", max_length=15, blank=False)
    description = models.CharField(verbose_name="Описание", max_length=300, blank=False)
    date_time = models.DateTimeField
    status = models.CharField(
        "Статус", max_length=1, choices=Status, default=Status.NEW
    )
    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name="Заявитель",
    )
    date_time = models.DateTimeField(
        "Дата и время", blank=False, validators=[statement_date_time_only_hours]
    )