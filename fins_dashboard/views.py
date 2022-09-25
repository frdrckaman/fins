from .mixin import FinServicesAdmin


class HomeView(FinServicesAdmin):
    template_name = f"fins_dashboard/bootstrap/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

