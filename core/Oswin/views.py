from django.shortcuts import render

from pathlib import Path
from django.http import HttpResponse


def index(_):
    p = Path(__file__).parent / "index.html"
    with p.open("r", encoding = 'utf-8') as f:
        return HttpResponse(f.read())
