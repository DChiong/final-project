from django.db import models

# Create your models here.
class StudentRecord(models.Model):
    student_id = models.CharField(max_length=255)
    study_hours = models.CharField(max_length=255)
    previous_exam_score = models.CharField(max_length=255)
    pass_fail = models.BooleanField()  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = 'Pass' if self.pass_fail else 'Fail'
        return f"{result} - Hours: {self.study_hours}, Score: {self.previous_exam_score}"

