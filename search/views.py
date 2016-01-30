from django.shortcuts import render
from search.forms import SearchForm
from search.dumpdata import dump

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    # dump()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            zipcode = form.cleaned_data["zipcode"]
            hosp_type = form.cleaned_data["hosp_type"]
            emergency = form.cleaned_data["emergency"]
            criteria = form.cleaned_data["criteria"]

            print(zipcode, hosp_type, emergency, criteria)
            return render(request, "search/result.html", {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, "search/index.html", {'form': form})