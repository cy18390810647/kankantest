# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.


class TDGatherData(models.Model):
    item_id = models.PositiveIntegerField(verbose_name=u"监控项ID")
    instance_id = models.PositiveIntegerField(verbose_name=u"监控实例ID", null=True)
    gather_time = models.DateTimeField(verbose_name=u"采集时间", null=True,auto_now_add=True)
    data_key = models.CharField(max_length=50, verbose_name=u"数据KEY", null=True)
    data_value = models.CharField(max_length=5000, verbose_name=u"数据VALUE", null=True)
    gather_error_log = models.CharField(max_length=5000, verbose_name=u"采集错误日志", null=True)
    score = models.PositiveIntegerField(verbose_name=u'分值', null=True)
    class Meta:
        db_table = 'td_gather_data'
