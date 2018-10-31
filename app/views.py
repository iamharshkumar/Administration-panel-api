from django.shortcuts import render,redirect
from .forms import playerform
import requests
from .forms import LoginForm,player,money,setwinner,join
from .forms import status
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
hostUrl = "http://www.pubg100.tk"

@login_required(login_url='login')
def tournamentform(request):
    form = playerform(request.POST or None)
    message = ""
    context = {
        "title":"Tournament",
        "form":form
    }
    
    if form.is_valid():
        print(form.cleaned_data)
        name = request.POST.get('name')
        match = request.POST.get('match')
        room_id = request.POST.get('room_id')
        room_pass = request.POST.get('room_pass')
        max_player = request.POST.get('max_player')
        fee = request.POST.get('fee')
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')
        p3 = request.POST.get('p3')
        p4 = request.POST.get('p4')
        p5 = request.POST.get('p5')
        p6 = request.POST.get('p6')
        start_at = request.POST.get('start_at')
        
        print(name)
        print(match)
        print(room_id)
        print(room_pass)
        print(max_player)
        print(fee)
        print(p1)
        print(p2)
        print(p3)
        print(p4)
        print(p5)
        print(p6)
        print(start_at)
        
        
        url = hostUrl + "/createTournament.php"


        response = requests.post(url, data={'name':name, 
                                'match':match, 
                                'room_id':room_id,
                                'room_pass':room_pass, 
                                'max_player':max_player, 
                                'fee':fee,
                                'p1':p1, 
                                'p2':p2,
                                'p3':p3,
                                'p4':p4,
                                'p5':p5,
                                'p6':p6,
                                'start_at':start_at,
                                'token':'5bb30fe31eabe0.80549502'}).json()
        
        message = response["Message"]
        
    return render(request,"form.html",{"message":message,"form":form})

   
def loginpage(request):
    form = LoginForm(request.POST or None)
    context = {
        "title":"Login",
        "form":form
    }
    
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            context['form'] = LoginForm()
            return redirect("/dashboard")
        else:
            print("error")
            
    return render(request,"login.html",context)    

@login_required(login_url='login')    
def dashboard(request):
    return render(request,"dashboard.html")
    
    

@login_required(login_url='login')
def player_details(request):
    form = player(request.POST or None)
    released = ""

    if form.is_valid():
        # email = request.POST.get('email')
        pubg_id = request.POST.get('pubg_id')
    
        url =   hostUrl + '/getUserDetails.php'

        response = requests.post(url, data={
                                            'pubg_id':pubg_id,
                                            'token':'5bb30fe31eabe0.80549502'}).json()
        released =  response['List']      

        
    return render(request,"playersearch.html",{"form":form,"released":released})
                
@login_required(login_url='login')
def money_trans(request):
    form = money(request.POST or None)
    result = ""
    
    if form.is_valid():
        trans_id = request.POST.get('trans_id')
        amount = request.POST.get('payment')
        
        
        url=  hostUrl + '/createPayment.php'

        response = requests.post(url, data={
                                'transId':trans_id,
                                'amount':amount,
                                'token':'5bb30fe31eabe0.80549502'}).json()
        result =  response['Message']
    
    
    return render(request,"money.html",{"result":result,"form":form})    

@login_required(login_url='login')    
def winner(request):
    
    
    url=  hostUrl + '/get_tournament_list.php'


    response = requests.post(url,data={
                                        'status':'2',
                                        
        
                                      }).json()



    data = response['List']
    
    return render(request,"setwinner.html",{"data":data})

@login_required(login_url='login')    
def position(request):
    
    form  = setwinner(request.POST or None)
    msg = ""
    
    if form.is_valid():
        
        tournament_id = request.POST.get('tournament_id')
        pubg_id = request.POST.get('pubg_id')
        position = request.POST.get('position')
        
        import requests
        url=   hostUrl + '/setWinner.php'


        response = requests.post(url, data={
                                'tournamentId':tournament_id,
                                'pubg_id':pubg_id,
                                'position':position,
                                'token':'5bb30fe31eabe0.80549502'}).json()
                                
        msg = response['Message']   
        
    return render(request,"position.html",{"data":msg,"form":form})
    
def playerjoin(request):
    form = join(request.POST or None)
    msg = ""
    
    if form.is_valid():
        tournament_id = request.POST.get('tournament_id')
        
        url=   hostUrl + '/getPlayerList.php'


        response = requests.post(url, data={
                                'tournamentId':tournament_id,
                                'token':'5bb30fe31eabe0.80549502'}).json()
                                
        msg = response['List']
        
    return render(request,"join.html",{"form":form,"msg":msg})    

      
def tournament(request):
    form = status(request.POST or None)
    msg = ""
    
    if form.is_valid():
        
        tournament_id = request.POST.get('tournament_id')
        status_tournament = request.POST.get('status')
        
        tournamentUrl =  hostUrl + '/setTournamentStatus.php'


        response = requests.post(tournamentUrl, data={
                                'tournamentId':tournament_id,
                                'status':status_tournament,
                                'token':'5bb30fe31eabe0.80549502'}).json()
                                
        msg = response['Message']
    
    return render(request,"status.html",{"form":form,"msg":msg})    