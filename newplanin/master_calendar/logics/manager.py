from django.shortcuts import get_object_or_404
from master_calendar.logics.tools import *
from master_calendar.models import *
from master_calendar.logics.tools import *

def on_save_slots(pid, slots):
    
    project = Project.objects.get(pid=pid);
    users = list(project.users.all())
    user = slots[0].creator
    user_idx = users.index(user)

    posting_info = list(project.user_posting_info.all())[user_idx]
    posting_info.has_posted = True
    posting_info.save()

    has_not_posted = 0
    everyone_has_posted = True

    for u in project.user_posting_info.all():
        if u.has_posted == False:
            everyone_has_posted = False
            has_not_posted += 1
            # break

    if everyone_has_posted:
        print('모두가 업로드 완료함')

        slots = Tools.merge(Tools.sort(users[0].user_created_slots.all()))
        for i in range(1, len(users)):
            slots = Tools.intersect(slots, Tools.merge(Tools.sort(users[i].user_created_slots.all())))

            if len(slots) == 0:
                print('겹치는 일정이 없습니다.')
                return

        i = 0
        for s in slots:
            i += 1
            print(f"{i}: {s.start_timedate} ~ {s.end_timedate}")
        
    else:
        print(f'아직 미제출 있음 : {has_not_posted}명')

    print('end of program')
    return
    