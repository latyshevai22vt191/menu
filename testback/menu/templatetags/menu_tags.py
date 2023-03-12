from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.filter(name='times')
def times(number):
    return range(number)


@register.simple_tag
def draw_menu(type,context):
    template = '{template_name}.html'.format(template_name=type)
    context = {'categories':context}
    return render_to_string(template, context)
