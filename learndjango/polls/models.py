from django.db import models
from rest_framework import serializers


class Subject(models.Model):
    no = models.AutoField(primary_key=True, db_comment="学科编号")
    name = models.CharField(max_length=50, db_comment="学科名称")
    intro = models.CharField(max_length=1000, db_comment="学科介绍")
    is_hot = models.IntegerField(db_comment="是不是热门学科")

    class Meta:
        managed = False
        db_table = "tb_subject"


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"


class SubjectSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ("no", "name")


class Teacher(models.Model):
    no = models.AutoField(primary_key=True, db_comment="老师编号")
    name = models.CharField(max_length=20, db_comment="老师姓名")
    sex = models.IntegerField(db_comment="老师性别")
    birth = models.DateField(db_comment="出生日期")
    intro = models.CharField(max_length=1000, db_comment="老师介绍")
    photo = models.CharField(max_length=255, db_comment="老师照片")
    good_count = models.IntegerField(
        default=0, db_column="gcount", verbose_name="好评数"
    )
    bad_count = models.IntegerField(
        default=0, db_column="bcount", verbose_name="差评数"
    )
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column="sno")

    class Meta:
        managed = False
        db_table = "tb_teacher"


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        exclude = ("subject",)


class User(models.Model):
    """用户"""

    no = models.AutoField(primary_key=True, verbose_name="编号")
    username = models.CharField(max_length=20, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    tel = models.CharField(max_length=20, verbose_name="手机号")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    last_visit = models.DateTimeField(null=True, verbose_name="最后登录时间")

    class Meta:
        db_table = "tb_user"
        verbose_name = "用户"
        verbose_name_plural = "用户"
