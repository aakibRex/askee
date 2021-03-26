from django.urls import path

from . import views
app_name = 'app'
urlpatterns = [

    path('',views.appView,name='appview'),
    path('qna',views.searchQnA,name='searchQnA'),
    path('register_clg',views.rgstr_clg,name='register_clg'),
    path('clgRegistration',views.clg_registration,name='clg_registration'),
    path('ask',views.ask_ques,name='ask'),

    path('ansQues/<int:ques_id>/',views.answer,name='answer'),
    path('viewAns/<int:ques_id>',views.view_ans,name='viewAns'),
    path('user_questions', views.user_questions, name='user_questions'),
    path('user_ans', views.user_ans, name='user_answers'),

    path('delete_ques/<int:quesid>', views.delete_ques, name='delete_ques'),
    path('edit_ques/<int:quesid>', views.edit_ques, name='edit_ques_name'),

    path('delete_ans/<int:ansid>', views.delete_ans, name='delete_ans'),
    path('edit_ans/<int:ansid>', views.edit_ans, name='edit_ans'),

]