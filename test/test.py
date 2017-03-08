import os
import sys



basedir = (os.path.sep).join(os.path.abspath(__file__).split(os.path.sep)[:-2])
sys.path.append(basedir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'untitled1.settings'
import django

django.setup()



from polls.models import Question, Choice
from app01.models import *
from django.utils import timezone
import datetime


#
host_list = []
host_list.append(Host(name="server05",ip_addr="127.0.0.5"))
host_list.append(Host(name="server06",ip_addr="127.0.0.6"))
# #
Host.objects.bulk_create(host_list)
host_list = Host.objects.all()


for h in host_list:
    print h.name



# q = Question(question_text="What's new?", pub_date=timezone.now())
# q.save()


# question_list = Question.objects.all()
#
# for q in question_list:
#     print q.question_text
#
#
# for q in Choice.objects.all():
#     print q

# choice_list = q.choice_set.select_related()
#
#
# print choice_list


