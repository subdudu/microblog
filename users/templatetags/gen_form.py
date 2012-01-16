from django import template
from django.contrib.auth.forms import AuthenticationForm



register = template.Library()



@register.inclusion_tag('users/mini_profile.pt', takes_context=True)
def generate_authentication_form(context):
	form = AuthenticationForm()
	return {
			'form': form,
			'next': '/',
			'user': context['user'],
			}
