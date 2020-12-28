from urllib.parse import urlencode

from django.conf import settings
from django.shortcuts import render
import requests

from core.forms import SearchForm


def home(request):
    results = []
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            base_api_url = settings.QUERIDO_DIARIO_BASE_API_URL
            api_params = {
                "page": 1,
                "page_size": 1000,
            }
            if form.data["since"]:
                api_params["since"] = form.data["since"]
            if form.data["until"]:
                api_params["until"] = form.data["until"]
            if form.data["keywords"]:
                api_params["keywords"] = form.data["keywords"]

            if form.data["territory_id"]:
                territory_id = request.POST["territory_id"]
                base_api_url = f"{base_api_url}/gazettes/{territory_id}"
            else:
                base_api_url = f"{base_api_url}/gazettes/"

            encoded_params = urlencode(api_params)
            api_url = f"{base_api_url}?{encoded_params}"
            response = requests.get(api_url)
            results = response.json()
    else:
        form = SearchForm()

    context = {
        "form": form,
        "results": results,
    }

    return render(request, "home.html", context)
