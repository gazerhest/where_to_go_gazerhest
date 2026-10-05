from django.shortcuts import render, redirect
from django.http import Http404
from django.utils import timezone
from .forms import AddPlaceForm
import random

BASE_PLACES = [
    {
        'id': 1,
        'title': 'Cultural and Arts Center (КМЦ)',
        'description': "Usually, all kinds of events are held here, but every Friday absolutely nothing (nothing) happens here, and nothing happens at 18:00 on Friday - it’s just that on those days it called the 'на KMЦ'.",
        'place_type': 'Recreation / Education',
        'location': '',
        'rating': 5,
        'created_at': '13.09.2026'
    },
    {
        'id': 2,
        'title': 'FIDO HUB',
        'description': "Despite Mohyla Academy’s long history, students here are skilled in using modern technology, and many wanted to put that knowledge to work for the benefit of the academy - and that is how the student organization FIDO (some knows it as USIC) came into being",
        'place_type': 'Recreation / Education',
        'location': 'Voloska St, 8/5 (basement), Kyiv',
        'rating': 3,
        'created_at': '10.10.2025'
    },
    {
        'id': 3,
        'title': 'Lutsk',
        'description': "Life in a big city, such as Kyiv, with traffic jams, noise, pollution, and many other problems, can quickly throw a person off balance, and they’ll need time to recover. The city of Lutsk could be a great solution - it has two McDonald’s, three shopping malls with movie theaters, and one school. Instead of diesel vehicles, there are electric - scooters and nothing else. The population is relatively small, so you won’t have to worry about getting a good night’s sleep or getting to another part of the city without traffic jams.",
        'place_type': 'Cafe / Restruants',
        'location': 'Lutsk, Volynska oblast',
        'rating': 4,
        'created_at': '14.09.2026'
    },
]


def index(request):
    places = get_user_places(request)
    random_place = None

    if request.GET.get('random') == 'true' and places:
        k = [int(p.get('rating', 1)) for p in places]
        chosen_card = random.choices(places, weights=k, k=1)[0]
        random_place = display_card(chosen_card)
    context = {
        'random_place': random_place,
        'places': places
    }
    return render(request, 'places/index.html', context)


def get_user_places(request):
    if not request.session.get('places'):
        request.session['places'] = [place.copy() for place in BASE_PLACES]
    return request.session['places']


def display_card(place):
    display_place = place.copy()

    display_place['stars'] = '⭐' * int(place.get('rating', 1))
    location = place.get('location', '').strip()
    display_place['display_location'] = location if location else 'Secret place 👀'

    description_words = place.get('description', '').split()
    if len(description_words) > 6:
        display_place['pre_description'] = ' '.join(description_words[:6]) + '...'
    else:
        display_place['pre_description'] = place.get('description', '')

    return display_place


def place_list(request):
    raw_places = get_user_places(request)
    format_places = [display_card(place) for place in raw_places]

    return render(request, 'places/list.html', {'places': format_places})


def place_detail(request, place_id):
    places = get_user_places(request)
    raw_place = next((p for p in places if p['id'] == place_id), None)

    if not raw_place:
        raise Http404(f"Place with ID {place_id} not found")

    place = display_card(raw_place)
    return render(request, 'places/detail.html', {'place': place})


def add_place(request):
    if request.method == 'POST':
        form = AddPlaceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            places = get_user_places(request)
            next_id = max([p['id'] for p in places], default=0) + 1
            curr_date = timezone.localdate().strftime("%d.%m.%Y")

            new_place = {
                'id': next_id,
                'title': data['title'].strip(),
                'description': data['description'].strip(),
                'place_type': data['place_type'],
                'location': data['location'].strip(),
                'rating': data['rating'],
                'created_at': curr_date
            }

            places.append(new_place)
            request.session['places'] = places

            return redirect('places:list')
    else:
        form = AddPlaceForm()
    return render(request, 'places/add.html', {'form': form})
