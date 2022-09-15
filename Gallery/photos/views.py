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
    template_name = "photo.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Monkey D. Luffy',
            'body': 'My name is Luffy and I will become the Pirate King.',
            'image': '/static/images/luffy.jpg'
        }
