from django.shortcuts import render_to_response
from django.conf import settings


def search(request):
    template = getattr(settings, 'CSE_TEMPLATE', 'google_cse/default.html')
    cx_code = getattr(settings, 'CX_CODE', '')

    query = request.GET.get('q', '')
    context = {
        'CX_CODE': cx_code,
        'q': query,
    }

    return render_to_response(template, context)
