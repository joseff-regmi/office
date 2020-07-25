from django.shortcuts import render, redirect
from .forms import MemoForm


def entry_memo(request):
    if request.method == 'POST':
        form = MemoForm(request.POST or none)
        if form.is_valid():
            form.save()
        return redirect('/entry_memos.html')

    else:
        form = MemoForm()
    return render(request, "entry_memos.html", {'form': form})