from django.views.generic import RedirectView
from django.core.urlresolvers import reverse


class ErrorRedirect(RedirectView):
    """
        Redirect to index when raise errors ;-)
    """
    def get_redirect_url(self, *kwargs):
        return reverse('web.index')
