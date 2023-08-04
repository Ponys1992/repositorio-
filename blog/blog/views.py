from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def nosotros(request):
    return render(request,'nosotros.html',{
        "saludo":"Conocenos",
        "nombre":"Creemos que todas las personas deben tener acceso a productos de inversión sofisticados y honestos.Creemos que se puede atender bien.Partimos de esa premisa, y decidimos que el primer paso era armar un gran equipo. Para eso, hicimos un lugar de trabajo confortable, donde cada miembro de nuestro grupo se siente a gusto y contento de trabajar cada día. Solo así, nos aseguramos de que cada uno dé lo mejor de sí mismo. Atendemos prestando atención.Nuestros asesores te van a escuchar. Si no tenes muy claro el plan, vamos a ayudarte a diseñarlo. Vamos a conversar sobre tus expectativas y necesidades; vamos a hablar sobre horizonte de inversión y objetivos esperables en función de las distintas alternativas disponibles en el mercado de capitales, un lugar regulado y transparente.",
        "autor":"Blog De Economia",
    } )


# def login(request):
#     if request.method == 'POST':
#        email = request.POST.get('email')
#        password = request.POST.get('password')

#        print(email)
#        print(password)

#     return render(request, 'usuarios/login.html')