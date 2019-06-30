from django.shortcuts import render


def main(request):
    return render(request,'main/main_page.html',context=None)


def about(request):
    return render(request,'main/about_page.html',context=None)