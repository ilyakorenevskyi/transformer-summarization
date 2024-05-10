from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .summarize import summarize_text


def main_page(request):
    return render(request, 'main_page.html')


@csrf_exempt
def generate_summary(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            language = data.get('language')
            model = data.get('model')
            text = data.get('text')
            summary = summarize_text(language, model, text)
            return JsonResponse({'summary': summary})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return redirect('main_page')
