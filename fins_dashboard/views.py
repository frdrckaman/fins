from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = f"fins_dashboard/bootstrap/base.html"

    def get_context_data(self, **kwargs):
        pass

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

