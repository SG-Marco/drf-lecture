def article(request, animation_pk):
    if request.method =='POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        animation = Animation.objects.get(pk=animation_pk)
        article = Article(title=title, content=content, user=request.user, animation=animation)
        article.save()



        article = Article(**request.POST)