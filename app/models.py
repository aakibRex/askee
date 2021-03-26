from django.db import models


class quesInfo(models.Model):

    Qid = models.AutoField(primary_key=True)
    questions = models.TextField()
    asked_by_name = models.CharField(max_length=100)
    college_name = models.TextField()
    desig = models.CharField(max_length=50)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.questions


class ansInfo(models.Model):
    Qid = models.ForeignKey('quesInfo', default=None, on_delete=models.CASCADE)
    answers = models.TextField()
    ans_by_name = models.CharField(max_length=100)
    desig = models.CharField(max_length=100)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.answers


class clgInfo(models.Model):
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name
