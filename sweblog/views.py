from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts=[{
	'author':'Swetha',
	'title':'Blog Post1',
	'content':'First post content',
	'date_posted':'July 7,2020'

},
{
'author':'Sidhartha',
	'title':'Blog Post2',
	'content':'Second post content',
	'date_posted':'July 8,2020'
}
]


def home(request):
	context={
	'posts':Post.objects.all()
	}
	return render(request,'sweblog/home.html',context)



def about(request):
	return render(request,'sweblog/about.html',{'title':'About'})

# Create your views here.
