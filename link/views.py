from .check_symbols_slug import check_symbols

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.base_user import BaseUserManager
from django.views.decorators.csrf import csrf_exempt

from .models import Link
from .forms import AddLinkForm, SerchLinkForm

new_link = {}


def root(request, short_url):
    url = get_object_or_404(Link, short_url=short_url)
    url.amount_clicks += 1
    url.save()
    return redirect(url.received_url)


def prepare_link(request):
    slug = new_link.get('slug')
    new_url = request.build_absolute_uri(slug)
    context = {
        'new_url': new_url
    }
    return render(request, 'link/prepare_link.html', context)


@csrf_exempt
def add_link(request):
    if request.method == 'POST':
        form = AddLinkForm(request.POST)
        if form.is_valid():
            slug = form.cleaned_data.get('short_url')
            if not slug:
                slug = BaseUserManager().make_random_password()
            else:
                coincidence = check_symbols(slug)
                if not coincidence:
                    form.add_error(
                        None, f'Ваша новая ссылка содержит запрещенные символы'
                    )
                    return render(request, 'link/create_link.html',
                                  {'form': form})
            try:
                Link(
                    received_url=form.cleaned_data.get('received_url'),
                    short_url=slug
                ).save()
                new_link['slug'] = slug
                return redirect('prepare_link')
            except:
                form.add_error(
                    None, f'Данная ссылка уже существует'
                )
    else:
        form = AddLinkForm()
    return render(request, 'link/create_link.html', {'form': form})


def show_links(request):
    return render(request, 'link/show_links.html')


def index(request):
    return render(request, 'link/index.html')


@csrf_exempt
def search_about_links(request):
    if request.method == 'POST':
        form = SerchLinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            found_links = Link.objects.find_url(link)
    else:
        form = SerchLinkForm()
        found_links = None

    return render(
        request, 'link/search_about_links.html',
        {'form': form, 'found_links': found_links}
    )
