from django.shortcuts import render


def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        return render(request, "index.html", {"text": text})
    return render(request, "index.html", {})

