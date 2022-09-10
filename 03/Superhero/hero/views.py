from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class IchigoView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Ichigo Kurosaki',
            'body': 'My name is Ichigo and I will protect my loved ones.',
            'image': '/static/images/ichigo.jpg'
        }


class LuffyView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Monkey D. Luffy',
            'body': 'My name is Luffy and I will become the Pirate King.',
            'image': '/static/images/luffy.jpg'
        }


class NarutoView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Naruto Uzumaki',
            'body': 'My name is Naruto and I will become the Hokage.',
            'image': '/static/images/naruto.jpg'
        }
