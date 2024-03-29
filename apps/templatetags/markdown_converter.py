import markdown
from django import template

register = template.Library()


@register.filter
def convert_markdown(value):
    return markdown.markdown(value, extensions=['fenced_code', 'codehilite', 'tables', 'nl2br', 'toc',
                                                'attr_list'])
