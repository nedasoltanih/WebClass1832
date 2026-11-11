from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, db_column="text")
    pub_date = models.DateTimeField("date published")
    # q_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True,
                              verbose_name="email address")
    language = models.CharField(max_length=2, default="en",
                                choices=[("en", "English"),
                                         ("fa", "Farsi"),
                                         ("ar", "Arabic"),])
    name = models.CharField(max_length=200, null=True, blank=True, help_text="Name of asking person")
    # picture = models.ImageField(upload_to="polls/pictures",null=True,blank=True,)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text