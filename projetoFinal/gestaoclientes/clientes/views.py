from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .form import PersonForm

# Create your views here.


@login_required
def person_list(request):
    termo_busca = request.GET.get('pesquisa', None)
    
    if termo_busca:
        persons = Person.objects.all()
        persons = persons.filter(first_name=termo_busca)
    else:
        persons = Person.objects.all()    
    
    return render(
        request, 'person.html', {'persons':persons}
    )

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("person_list")
    return render(request, "person_form.html", {"form": form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(
        request.POST or None, request.FILES or None, instance=person
    )

    if form.is_valid():
        form.save()
        return redirect("person_list")

    return render(request, "person_form.html", {"form": form, "pessoa":person})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(
        request.POST or None, request.FILES or None, instance=person
    )

    if request.method == "POST":
        person.delete()
        return redirect("person_list")

    return render(request, "person_delete_confirm.html", {"form": form})


def return_list(request):
    return redirect("person_list")


def back_home(request):
    return redirect("homepage")
