import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter             # sub 함수에 @register.filter 애너테이션 적용시, 템플릿에서 해당 함수를 필터로 사용 가능
def sub(value, arg):
    return value - arg       # sub 필터는 기존 값 value에서 입력으로 받은 값 arg를 빼서 리턴


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]    # nl2bar : 줄바꿈 문자를 <br>로 바꿔줌, fenced_code : 마크다운의 소스코드 표현('''''')을 위해 필요
    return mark_safe(markdown.markdown(value, extensions=extensions))
