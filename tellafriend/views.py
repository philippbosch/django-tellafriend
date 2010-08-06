from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Template
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from django.contrib.sites.models import Site

from tellafriend.forms import TellAFriendForm

def tellafriend(request):
    """Displays the tell-a-friend form and sends out the e-mail"""
    if request.method == 'POST':
        form = TellAFriendForm(request.POST)
        if form.is_valid():
            text_content = render_to_string('tellafriend/email.txt', request.POST, context_instance=RequestContext(request))
            html_content = render_to_string('tellafriend/email.html', request.POST, context_instance=RequestContext(request))
            msg = EmailMultiAlternatives(_("Recommendation by %s" % request.POST.get('email_sender')), text_content, request.POST.get('email_sender'), [request.POST.get('email_recipient')])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect(reverse('tellafriend_success'))
    else:
        form = TellAFriendForm()
    
    if request.REQUEST.has_key('url'):
        url = 'http://%s%s' % (Site.objects.get_current().domain, request.REQUEST['url'])
    else:
        url = 'http://%s' % (Site.objects.get_current().domain,)
    
    form.fields['url'].initial = url
    return render_to_response('tellafriend/tellafriend.html', {'tellafriend_form': form, 'tellafriend_url': url}, context_instance=RequestContext(request))