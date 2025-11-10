from django.shortcuts import render
/*criando hello-word*/
def hello_view(request):
    return render(request, 'meuapp/hello.html')
