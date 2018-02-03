from django.db import models
from django.contrib.auth.models import User
# from django.contrib import admin

# Create your models here.


class Manufacturers(models.Model):
    """廠商類"""
    name = models.CharField(max_length=50, verbose_name="廠商名")
    cellphone = models.CharField(max_length=20, verbose_name="電話")
    email = models.EmailField()
    address = models.CharField(max_length=200, verbose_name="地址")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '廠商名單'
        verbose_name_plural = verbose_name


class Pictures(models.Model):
    """照片類"""
    order = models.ForeignKey("RepairOrders", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="images/", verbose_name="維修單照片")

    def __str__(self):
        return self.picture.name

    class Meta:
        verbose_name = "維修單照片"
        verbose_name_plural = verbose_name


class RepairOrders(models.Model):
    """維修單類"""
    employee = models.ForeignKey(User)
    serial_number = models.CharField(max_length=50)
    working_status_choices = (
        ("已完成", "已完成"),
        ("處理中", "處理中"),
    )
    status = models.CharField(max_length=50, choices=working_status_choices, default="處理中")
    manufacturer = models.ForeignKey(Manufacturers)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="訂單創建時間")
    last_edited_time = models.DateTimeField(auto_now=True, verbose_name="訂單最後修改時間")
    note = models.TextField(blank=True, verbose_name="備註")

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name = '維修單'
        verbose_name_plural = verbose_name
