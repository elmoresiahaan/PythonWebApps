from pathlib import Path
from django.views.generic import TemplateView


def photo_list():
    def photo_details(i, f):

        caption = f'Caption for Photo {i}'
        return dict(id=i, file=f, caption=caption)

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        return dict(photo=p)


class LuffyView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Monkey D. Luffy',
            'image': '/static/images/33.jpg',
            'strength1': 'conqueror\'s haki',
            'strength2': 'immense physical strength',
            'strength3': 'endurance and stamina',
            'weakness1': 'impulsiveness',
            'weakness2': 'prone to cutting or stabbing',
            'weakness3': 'fire and ice',
        }


class NarutoView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Naruto Uzumaki',
            'image': '/static/images/11.jpg',
            'strength1': 'all elements of chakra',
            'strength2': 'sage mode',
            'strength3': 'nine-tailed beast',
            'weakness1': 'no skills in genjutsu',
            'weakness2': 'too naive',
            'weakness3': 'lack of ninjutsu diversity',
        }


class SaitamaView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Saitama (Caped Baldy)',
            'image': '/static/images/22.jpg',
            'strength1': 'composure',
            'strength2': 'shock-wave',
            'strength3': 'speed and athleticism',
            'weakness1': 'lack of technique and training in martial arts',
            'weakness2': 'still human',
            'weakness3': 'terrible at video games',
        }


class TanjiroView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Tanjiro Kamado',
            'image': '/static/images/44.jpg',
            'strength1': 'immense stamina',
            'strength2': 'endurance',
            'strength3': 'control oxygen level',
            'weakness1': 'too honest',
            'weakness2': 'memory loss',
            'weakness3': 'keeping sword intact',
        }


class NatsuView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Natsu Dragneel',
            'image': '/static/images/55.jpg',
            'strength1': 'ability to consume flames',
            'strength2': 'immune to explosions',
            'strength3': 'fire dragon slayer magic',
            'weakness1': 'motion sickness',
            'weakness2': 'not planning ahead',
            'weakness3': 'impulsive and hasty',
        }
