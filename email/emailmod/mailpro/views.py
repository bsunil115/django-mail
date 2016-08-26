from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,BadHeaderError

# Create your views here.
def index(request):
	subject=request.POST.get('subject','test mail')
	message=request.POST.get('message','hello world')
	from_email=request.POST.get('from_email','support@advoge.com')
	if subject and message and from_email:
		try:
			send_mail(subject,message,from_email,['jayan.indian@gmail.com'])
		except BadHeaderError:
			return HttpResponse('invalid header found')
		return HttpResponse('success')
	else:
		return HttpResponse("Please check your email parameters")