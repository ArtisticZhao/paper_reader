from django.shortcuts import render
from django.http import HttpResponse
from script import get_paper


# Create your views here.
def ckxx(request):
    #  return HttpResponse(u"hello")
    paper_dict = get_paper.get_ckxx_paperlist()
    return render(request, 'ckxx.html', {'paper_list': paper_dict})


def get_a_page(request):
    url = request.GET['url']
    title = request.GET['title']
    pic_links = get_paper.get_day_pic(url)
    # print(url)
    # print(pic_links)
    # return HttpResponse(u"hello")
    return render(request, 'all_in_one.html', {'pic_list': pic_links, 'title': title})
