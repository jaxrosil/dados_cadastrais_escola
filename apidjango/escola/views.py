from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {'id': 13, 'nome': "Jax"}
        return JsonResponse(aluno)
