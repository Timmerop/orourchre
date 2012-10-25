from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from deckocards.models import *

# def Home(request):

# 	template_args = {
# 		'deck' = deck(),
# 	}

# 	return render_to_response('index.html', template_args, context_instance=RequestContext(request))
