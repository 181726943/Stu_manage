import datetime

from django.db import models


# Create your models here.

class Student(models.Model):
    # 模型字段
    stu_ID = models.CharField(primary_key=True, max_length=12, blank=False, default="123456789", verbose_name="学号")
    stu_password = models.CharField(max_length=40, default="000000", verbose_name="用户密码")
    stu_name = models.CharField(max_length=40, blank=True, verbose_name="姓名")
    age = models.SmallIntegerField(default=0, verbose_name="年龄")
    sex = models.CharField(choices=(('Male', '男'), ('Female', '女')), max_length=6, default='Male', verbose_name="性别")
    department = models.CharField(max_length=40, blank=False, default="计算机", verbose_name="专业")
    classes = models.DateField(auto_now=True, blank=False, verbose_name="年级")
    email = models.EmailField(blank=True, verbose_name='邮箱')
    address = models.TextField(blank=True, verbose_name="家庭住址")
    enroll_time = models.DateField(auto_now=True, blank=False, verbose_name="入学时间")

    def __str__(self):
        return self.stu_name

    class Meta:
        db_table = "student"
        verbose_name = "学生管理"
        verbose_name_plural = verbose_name


class Course(models.Model):
    cou_name = models.CharField(primary_key=True, max_length=50, blank=False, verbose_name="课程名称")
    credit = models.IntegerField(blank=False, verbose_name="学分")
    open_term = models.DateField(default=datetime.date, blank=False, verbose_name="开设学期")

    def __str__(self):
        return self.cou_name

    class Meta:
        db_table = 'course'
        verbose_name_plural = verbose_name = "课程管理"


class Grade(models.Model):
    stu_ID = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="学生姓名")
    cou_name = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, verbose_name="课程名称")
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="分数")
    teacher = models.CharField(max_length=40, blank=False, verbose_name="任课教师")
    isretake = models.IntegerField(choices=((0, "否"), (1, "是")), default=0, verbose_name="重修标记")

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = "grade"
        verbose_name_plural = verbose_name = "成绩管理"


# 借阅图书
class Book(models.Model):
    bookId = models.CharField(primary_key=True, max_length=20, blank=False, verbose_name="图书ID")
    book_name = models.CharField(max_length=100, blank=False, verbose_name="图书名称")
    borrowDate = models.DateField(auto_now=True, blank=False, verbose_name="借阅日期")
    returnDate = models.DateField(auto_now=True, blank=False, verbose_name="归还日期")
    readStatus = models.CharField(choices=(("已读", "已读"), ("在读", "在读")), max_length=10, default="已读", verbose_name="图书状态")
    stu_ID = models.ForeignKey(Student, to_field="stu_ID", on_delete=models.CASCADE, verbose_name="读者ID")

    def __str__(self):
        return self.bookId

    class Meta:
        db_table = "图书管理"
        verbose_name_plural = verbose_name = "图书管理"


