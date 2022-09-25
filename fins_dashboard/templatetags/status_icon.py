from django import template

register = template.Library()


@register.inclusion_tag(
    f"fins_dashboard/bootstrap/status_icon.html",
    takes_context=True,
)
def FinStatusIcon(context, counter):
    ls = []
    x = counter - 1
    s_status = context.get('fin_services_status'),
    for status in s_status:
        ls.append(status)
    ls_status = ls[0]

    if ls_status[x] == 'UP':
        theme = 'bg-theme-9'
        icon = 'thumbs-up'
    else:
        theme = 'bg-theme-6'
        icon = 'alert-triangle'

    return {
        "theme": theme,
        "icon": icon,
    }
