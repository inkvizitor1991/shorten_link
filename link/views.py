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
    new_url = request.build_absolute_uri(f'/{slug}')
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
                link = Link(
                    received_url=form.cleaned_data.get('received_url'),
                    short_url=slug
                )
                link.save()
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
    root_url = request.build_absolute_uri('/')
    context = {
        'root_url': root_url
    }
    return render(request, 'link/show_links.html', context)


def index(request):
    return render(request, 'link/index.html')


@csrf_exempt
def search_about_links(request):
    root_url = request.build_absolute_uri('/')

    if request.method == 'POST':
        form = SerchLinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            found_links = Link.objects.find_url(link)
            context = {
                'form': form,
                'new_url': root_url,
                'found_links': found_links
            }
    else:
        form = SerchLinkForm()
        context = {
            'form': form
        }
    return render(
        request, 'link/search_about_links.html', context
    )
