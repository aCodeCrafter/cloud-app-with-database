from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5
class ChoiceInline(admin.StackedInline):
    model = Choice

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline,QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text','question_points',)
    list_filter = ['lesson']
    search_fields = ['question_text','question_points']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_content','correct_answer']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models
#  here
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
