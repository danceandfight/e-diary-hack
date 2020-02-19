import random

from datacenter.models import Schoolkid, Mark, Lesson, Chastisement, Commendation, Subject
from django.core.exceptions import MultipleObjectsReturned

def get_child(child_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
        return child
    except MultipleObjectsReturned:
        print('В школе несколько учеников с таким именем')
    except Schoolkid.DoesNotExist:
        print('Нет такого ученика')

def fix_marks(child_name):
    child = get_child(child_name)
    marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()

def remove_chastisements(child_name):
    child = get_child(child_name)
    chastisements = Chastisement.objects.filter(schoolkid=child)
    for chastisement in chastisements:
        chastisement.delete()

def create_commendation(child_name, chosen_subject):
    child = get_child(child_name)
    lesson = Lesson.objects.filter(year_of_study=child.year_of_study,
                                   group_letter=child.group_letter,
                                   subject__title=chosen_subject).order_by('-date')[0]
    with open('commendation_examples.txt', 'r', encoding='utf-8') as file:
        commendation_examples = [line.rstrip() for line in file]
    commendation_text = random.choice(commendation_examples)
    Commendation.objects.create(text=commendation_text,
                                created=lesson.date,
                                schoolkid=child,
                                subject=lesson.subject,
                                teacher=lesson.teacher)




