from django.shortcuts import render,redirect

# Create your views here.


def Home(request):
    
    lang_list= ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'markup', 'markup-templating', 'matlab', 'mongodb', 'objectivec', 'perl', 'php', 'powershell', 'python', 'r', 'regex', 'ruby', 'rust', 'sass', 'scala', 'sql', 'swift', 'yaml']
    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']
        return render(request, 'index.html',{'lang_list':lang_list, 'code':code, 'lang':lang})



    return render(request, 'index.html',{'lang_list':lang_list})