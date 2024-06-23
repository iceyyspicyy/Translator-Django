from django.shortcuts import render, HttpResponse
from translate import Translator


def home(request):
    if request.method == 'POST':
        text = request.POST["translate"]
        language = request.POST.get('language')
        translator = Translator(to_lang=language) 
        translation = translator.translate(text)  
        return render(request,'translate.html', {'translation':translation})
    return render(request, 'index.html')


