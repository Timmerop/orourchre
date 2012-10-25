from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

from deckocards.models import *

def home(request):
	hand1, hand2, hand3, hand4 = dealHand(deck())
	template_args = {
		'hand1' : hand1,
		'hand2' : hand2,
		'hand3' : hand3,
		'hand4' : hand4
	}

	return render_to_response('index.html', template_args, context_instance=RequestContext(request))
