from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AddReviewForm, SignUpForm, LoginForm, AddOrderForm, ContestSubmitionForm,RobotConfirmationForm, WithdrawForm, AddPackage_form
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    if  request.user.is_authenticated:
        if request.user.Is_client:
            return redirect('client_panel')
        if request.user.Is_worker:
            return redirect('user_panel')
    else:
        users = User.objects.all()
        users_count = users.count()
        order = Order.objects.all()
        order_count = order.count()
        rating = Review.objects.all()
        rating_count = rating.count()
        data = Review.objects.all()
        context = {
            'data' : data,
            'users' : users,
            'users_count' : users_count,
            'order' : order,
            'order_count' : order_count,
            'rating' : rating,
            'rating_count' : rating_count
    }
        return render(request, 'index.html',context)

def account_registration(request):
    if  request.user.is_authenticated:
        if request.user.Is_client:
            return redirect('client_panel')
        if request.user.Is_worker:
            return redirect('user_panel')
    else:    
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account created successfully!')
                return redirect('account_login')
        context = {'form':form}
        return render(request,'register.html', context)
    
def account_login(request):
    if  request.user.is_authenticated:
        if request.user.Is_client:
            return redirect('client_panel')
        if request.user.Is_worker:
            return redirect('user_panel')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =  request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None and user.Is_client:
                login(request, user)
                return HttpResponseRedirect('cpanel')
                # return redirect('client_panel')
            elif user is not None and user.Is_worker:
                login(request, user)
                return HttpResponseRedirect('panel')
            else:
                messages.info(request,'Incorrect username or password')
                return redirect('account_login')
            
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('account_login')
    
@login_required(login_url='account_login')
def client_panel(request):
    if request.user.is_authenticated:
        if request.user.Is_client: 
            order = Order.objects.filter(client=request.user.id)
            orders_count = order.count()
            if orders_count is not None:
                context = {'order':order, 'orders_count':orders_count}
            else:
                messages.success(request,'Currently, you have no order placed!')
            return render(request,'client_panel.html',context)
        elif request.user.is_authenticated and request.user.Is_worker:
            return HttpResponseRedirect('panel')
            
@login_required(login_url='account_login')
def user_panel(request):
    if request.user.is_authenticated:
        if request.user.Is_worker:   
            data = contest.objects.all()
            views = RobotConfirmationViews.objects.filter (champ_id= request.user.id)
            views_count = views.count()
            if views_count is not None:
                context = {'views':views, 'views_count':views_count, 'data':data}
                return render(request,'user_panel.html',context)
        elif request.user.is_authenticated and request.user.Is_client:
            return HttpResponseRedirect('cpanel')
            
@login_required(login_url='account_login')
def client_order(request):
    if request.user.is_authenticated:
        if request.user.Is_client:
            get_id = User.objects.filter(id=request.user.id)
            if len(get_id)>0:
                data = User.objects.get(id=request.user.id)
                context = {'data':data}
            form = AddOrderForm()
            if request.method == 'POST':
                form = AddOrderForm(request.POST,request.FILES)
                if form.is_valid:
                    data = form.save(commit=False)
                    login_user = User.objects.get(username=request.user.username)
                    data.client = login_user
                    data.save()
                    messages.success(request,'Order added successfully!')

            context = {'form':form}
            return render(request,'add_order.html', context)
        elif request.user.Is_worker:
            return HttpResponseRedirect('panel')
              
@login_required(login_url='account_login')
def watch_videos(request):
    if  request.user.is_authenticated:
        if request.user.Is_worker:
            get_id = User.objects.filter(id=request.user.id)
            if len(get_id)>0:
                data = User.objects.get(id=request.user.id)                   
                videos = AssignOrder.objects.filter(reciept = "VID101")
                form = RobotConfirmationForm()
                if request.method == 'POST':
                    form = RobotConfirmationForm(request.POST)
                    if form.is_valid:
                        data = form.save(commit=False)
                        login_user = User.objects.get(username=request.user.username)
                      
                        if RobotConfirmationViews.objects.filter(champ_id=login_user,entry_code= data).exists():
                            messages.success(request,'Task already completed..')
                        else:
                            data.champ_id = login_user
                            data.save()
                            messages.success(request,'Security confirmed! Click on start task now..')
                
            context = {'data':data,'videos':videos,'form':form}
            return render(request,'watch_videos.html',context)
        elif request.user.Is_client:
            return HttpResponseRedirect('cpanel')
             
def confirm_views(request):
    if request.user.is_authenticated:
        if request.user.Is_worker:
            get_id = User.objects.filter(id=request.user.id)
            if len(get_id)>0:
                data = User.objects.get(id=request.user.id)
                id = request.GET['vid']
                obj = AssignOrder.objects.get(assign_id=id)
            videos = AssignOrder.objects.all()
                
            context = {'data':data, 'videos':videos, 'obj':obj}
            return render(request,'confirm_task.html',context)
        elif request.user.Is_client:
            return HttpResponseRedirect('cpanel')
            
@login_required(login_url='account_login')
def post_likes(request):
    if request.user.is_authenticated:
        if request.user.Is_worker:
            data = AssignOrder.objects.filter(reciept='FOL101')
            context = {'data':data}
            return render(request,'user_likes.html',context)
        elif request.user.Is_client:
            return HttpResponseRedirect('cpanel')
        
@login_required(login_url='account_login')
def page_follows(request):
    if request.user.is_authenticated:
        if request.user.Is_worker:
            return render(request,'page_follow.html')
        if request.user.Is_client:
            return HttpResponseRedirect('cpanel')
        
@login_required(login_url='account_login')
def add_review(request):
    if request.user.is_authenticated:
        if request.user.Is_worker:
            get_id = User.objects.filter(id=request.user.id)
            if len(get_id)>0:
                data = User.objects.get(id=request.user.id)
                context = {'data':data}      
            form = AddReviewForm()  
            if request.method == 'POST':
                form = AddReviewForm(request.POST)
                if form.is_valid:
                    data = form.save(commit=False)
                    login_user = User.objects.get(username=request.user.username)
                    if Review.objects.filter(user_id=login_user).exists():
                        messages.success(request,'Review already exist..')
                    else:
                        data.user_id = login_user
                        data.save()
                        messages.success(request,'Thank you! Review Submitted..')
                    
            context = {'form':form}   
            return render(request,'reviews.html',context)
        if request.user.Is_client:
            return HttpResponseRedirect('cpanel')
           
@login_required(login_url='account_login')
def contest_submition(request):
    if request.user.is_authenticated:
        if request.user.Is_worker:
            get_id = User.objects.filter(id=request.user.id)
            if len(get_id)>0:
                data = User.objects.get(id=request.user.id)
            context = {'data':data}
            form = ContestSubmitionForm()  
            if request.method == 'POST':
                form = ContestSubmitionForm(request.POST,request.FILES)
                if form.is_valid():
                    data = form.save(commit=False)
                    login_user = User.objects.get(username=request.user.username)
                    if ContestEntries.objects.filter(user_name=login_user).exists():
                        messages.success(request,'Entry already exists..')
                    else:
                        data.user_name = login_user
                        data.save()
                        messages.success(request,'Congratulations! you made an entry..')
                    
            context = {'form':form}   
            return render(request,'contest_entry.html',context)
        elif request.user.Is_client:
            return HttpResponseRedirect('cpanel')
            
def FAQs(request):
    data = FrequentlyAskQuestions.objects.all()
    return render(request,'faq.html',context={'data':data})

def withdraw(request):
    if  request.user.is_authenticated:
        if request.user.Is_worker:   
            get_id = User.objects.filter(id=request.user.id)
            if len(get_id)>0:
                data = User.objects.get(id=request.user.id)
                context = {'data':data}
            form = WithdrawForm()
            if request.method == 'POST':
                form = WithdrawForm(request.POST)
                if form.is_valid:
                    data = form.save(commit=False)
                    login_user = User.objects.get(username=request.user.username)
                    data.user_name = login_user
                    data.save()
                    messages.success(request,'successfully!')

            order = WithdrawAmount.objects.filter(user_name=request.user.id)
            orders_count = order.count()
            if orders_count is  None:
                messages.success(request,'Currently, you have no order placed!')

            context = {'form':form, 'order':order, 'orders_count':orders_count}
            return render(request,'withdraw.html', context) 
        elif request.user.is_authenticated and request.user.Is_client:
            return HttpResponseRedirect('cpanel')
               
def confirm_task(request):
      if  request.user.is_authenticated:
        if request.user.Is_worker:
           system = request.POST.get('system',None)  
           data = User.objects.get(id=request.user.id)
           form = RobotConfirmationForm()
           if request.method == 'POST':
               form = RobotConfirmationForm(request.POST)
               if form.is_valid():
                    data = form.save(commit=False)
                    login_user = User.objects.get(username=request.user.username)
                    if RobotConfirmationViews.objects.filter(champ_id=login_user,entry_code=data):
                       messages.success(request,'Hey '+ str(login_user) + '! You have already completed this task.')
                       storeInput = int(data.entry_code)
                       print(system,storeInput,"checking")
                    else:
                            data.champ_id = login_user
                            data.entery_code = system
                            data.save()
                            messages.success(request,'Task confirmed! your earned 1 PKR..')   
                            return HttpResponseRedirect('../videos')
                            
           context = {'form':form, 'data':data}
           context['system'] = system
           return render(request,'confirm_task.html',context)
        elif request.user.Is_client:
            return HttpResponseRedirect('cpanel') 

def feedback(request):
     data = Review.objects.all().order_by('id')
     paginator = Paginator(data,6   )
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     context = {
        'page_obj' : page_obj,
     }
     return render(request, 'feedback.html',context)
 
def watch(request):
    if request.user.is_authenticated:
        if request.user.Is_worker:
            video = request.POST.get('video',None)  
            context = {}
            context['video'] = video    
            return render(request,'counter.html', context)
        
        elif request.user.Is_client:
            return HttpResponseRedirect('cpanel')
            