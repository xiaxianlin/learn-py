from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest, HttpResponse
from polls.models import (
    Subject,
    Teacher,
    User,
    SubjectSerializer,
    TeacherSerializer,
    SubjectSimpleSerializer,
)
from polls.utils import gen_random_code, gen_md5_digest
from polls.captcha import Captcha
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(("GET",))
def show_subjects(request: HttpRequest) -> HttpResponse:
    subjects = Subject.objects.all().order_by("no")
    # 创建序列化器对象并指定要序列化的模型
    serializer = SubjectSerializer(subjects, many=True)
    # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response(serializer.data)


@api_view(("GET",))
def show_teachers(request: HttpRequest) -> HttpResponse:
    try:
        sno = int(request.GET.get("sno"))
        subject = Subject.objects.only("name").get(no=sno)
        teachers = (
            Teacher.objects.filter(subject=subject).defer("subject").order_by("no")
        )
        subject_seri = SubjectSimpleSerializer(subject)
        teacher_seri = TeacherSerializer(teachers, many=True)
        return Response({"subject": subject_seri.data, "teachers": teacher_seri.data})
    except (TypeError, ValueError, Subject.DoesNotExist):
        return Response(status=404)


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    if request.session.get("userid"):
        try:
            tno = int(request.GET.get("tno"))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith("/praise/"):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {"code": 20000, "mesg": "投票成功", "count": count}
        except (ValueError, Teacher.DoesNotExist):
            data = {"code": 20001, "mesg": "投票失败"}
    else:
        data = {"code": 20002, "mesg": "请先登录"}
    return JsonResponse(data)


def login(request: HttpRequest) -> HttpResponse:
    hint = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session["userid"] = user.no
                request.session["username"] = user.username
                return redirect("/")
            else:
                hint = "用户名或密码错误"
        else:
            hint = "请输入有效的用户名和密码"
    return render(request, "login.html", {"hint": hint})


def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    request.session["captcha"] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type="image/png")


def logout(request):
    """注销"""
    request.session.flush()
    return redirect("/")
