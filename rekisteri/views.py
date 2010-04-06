# Create your views here.
from django.http import HttpResponse
from jasenrekisteri.rekisteri.models import Member
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

def index(request):
  member_list = Member.objects.all().order_by('-id')[:5]
  return render_to_response('members/index.html', {'member_list': member_list})

def detail(request, member_id):
  p = get_object_or_404(Member, pk=member_id)
  return render_to_response('members/detail.html', {'member': p})

