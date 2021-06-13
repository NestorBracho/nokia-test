from django.views import generic
from .forms import ParamsForm


class NokiaTestView(generic.FormView):
    template_name = 'nokia_app/nokia_test.html'
    form_class = ParamsForm

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        return self.render_to_response(self.get_context_data(**form.calculate()))

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super().get_context_data(**kwargs)
