from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

# Create your views here.

def index(request):
	comments = Comment.objects.order_by('-date')
	context = {'comments': comments}
	return render(request, 'guestbook/index.html', context)

def sign(request):
	if request.method == 'POST':
		form=CommentForm(request.POST) #instantiates the form again
		if form.is_valid():
			new_comment = Comment(name=request.POST['name'], comment= request.POST['comment'])#will create a new comment for the data base
			new_comment.save() # to save it to the data base
			return redirect('index')
	else:
		form=CommentForm()		

	form = CommentForm()
	context ={'form':form}
	return render(request, 'guestbook/sign.html', context)

