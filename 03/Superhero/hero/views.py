from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class SpidermanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman.jpg'
        }


class CaptainAmericaView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Captain America',
            'body': 'My name is Captain America',
            'image': '/static/images/capamerica.jpg'
        }


class NarutoView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Naruto Uzumaki',
            'body': 'My name is Naruto Uzumaki',
            'image': '/static/images/naruto.jpg'
        }
