from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import redirects
# from django.urls import reverse
from django.urls import reverse


from .models import clgInfo, quesInfo, ansInfo

def appView(request):
    ques = None
    user_id = 0

    clg_names = clgInfo.objects.all()
    if request.user.is_authenticated:
        ques = None
        user_clg = request.user.id
        ques = quesInfo.objects.filter(user_id=user_id)

    return render(request, 'home.html', {'clg_names': clg_names, 'ques': ques, 'uid': user_id , })

def searchQnA(request):
    show_edit = False

    clgName = request.POST.get('clgName')
    questions = quesInfo.objects.filter(college_name=clgName)


    return render(request, 'qna.html', {'clgName': clgName, 'ques': questions})

def rgstr_clg(request):
    return render(request, 'clg_rgstr_form.html')

def clg_registration(request):
    clg_name = request.POST['clgName']
    new_clg = clgInfo(college_name=clg_name)
    new_clg.save()

    return redirect('/')

def ask_ques(request):
    clg_names = clgInfo.objects.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            asked_by_name = request.user.name
            college_name = request.user.college_name
            desig = request.POST['desig']
            questions = request.POST['ques']
            user_id = request.user.id

            new_question = quesInfo(questions=questions, asked_by_name=asked_by_name, college_name=college_name,
                                    desig=desig, user_id=user_id)
            new_question.save()
            return redirect('/')
        else:
            return redirect("login")
    else:
        return render(request, "ask.html", {'clg_names': clg_names})

def answer(request, ques_id):
    if request.method == 'POST':

            Qid_id = ques_id
            answers = request.POST['ans']
            desig = request.POST['desig']
            ans_by_name = request.user.name
            user_id = request.user.id
            new_ans = ansInfo(answers=answers, ans_by_name=ans_by_name, desig=desig, Qid_id=Qid_id, user_id=user_id)
            new_ans.save()
            #print(ques_id,type(ques_id),str(ques_id))
            #print(reverse('nspace:viewAns',args=str(Qid_id)))
            return redirect("nspace:viewAns", ques_id=str(ques_id))

    else:
        if request.user.is_authenticated:
            return render(request, 'ans.html', {'qid': ques_id})
        else:
            url = reverse('nroute:login_user')
            nxt = request.GET.get("next", None)
            print(nxt,"in view ans")
            if nxt is not None:
                url += '?next=' + nxt
            return redirect(url)

def view_ans(request, ques_id):
    if request.user.is_authenticated:
        ques_answers = ansInfo.objects.filter(Qid_id=ques_id)
        ques_query = quesInfo.objects.filter(Qid=ques_id)
        asked_by = None
        ques = None
        college_name = None
        desig = None
        ans_by_stu_clg_name = request.user.college_name
        for q in ques_query:
            asked_by = q.asked_by_name
            ques = q.questions
            college_name = q.college_name
            desig = q.desig
        return render(request, 'answers.html',
                      {'As': ques_answers, 'Qs': ques, 'askedby': asked_by, 'clg': college_name,
                       'ans_clg_name': ans_by_stu_clg_name, 'desig': desig})
    else:
        #print(reverse('nroute:login_user'))
        url = reverse('nroute:login_user')
        nxt = request.GET.get("next", None)
        #print(nxt+"in view ans")
        if nxt is not None:
            url += '?next=' + nxt
        return redirect(url)

def user_questions(request):
    global user_ques
    if request.user.is_authenticated:
        user_ques = quesInfo.objects.filter(user_id=request.user.id)
    return render(request, 'questions_asked.html', {'questions': user_ques})

def delete_ques(request, quesid):
    obj = quesInfo.objects.filter(Qid=quesid)
    obj.delete()
    return redirect(reverse('nspace:user_questions'))

def edit_ques(request, quesid):
    if request.method == 'POST':
        edit = request.POST['edited_ques']
        ques_query = quesInfo.objects.get(Qid=quesid)
        ques_query.questions = edit
        ques_query.save()
        return redirect(reverse('nspace:user_questions'))
    else:
        ques = None
        ques_query = quesInfo.objects.filter(Qid=quesid)
        for q in ques_query:
            ques = q.questions
            quesid = q.Qid
        return render(request, 'edit_ques_page.html', {'ques': ques,'qid':quesid})
def user_ans(request):
    global user_ans
    if request.user.is_authenticated:
        user_ans = ansInfo.objects.select_related('Qid').all().filter(user_id=request.user.id)
    return render(request, 'user_ans.html', {'answers': user_ans})

def delete_ans(request, ansid):
    obj = ansInfo.objects.filter(id=ansid)
    obj.delete()
    return redirect(reverse('nspace:user_answers'))


def edit_ans(request, ansid):
    if request.method == 'POST':
        edit = request.POST['edited_ans']
        ans_query = ansInfo.objects.get(id=ansid)
        ans_query.answers = edit
        ans_query.save()
        return redirect(reverse('nspace:user_answers'))
    else:
        ans = None
        aid= 0
        ans_query = ansInfo.objects.filter(id=ansid)
        for a in ans_query:
            ans = a.answers
            aid = a.id
        return render(request, 'edit_ans_page.html', {'ans': ans,'aid':aid})

