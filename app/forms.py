from django import forms

class playerform(forms.Form):
    name = forms.CharField(max_length=20)
    match = forms.IntegerField()
    room_id = forms.IntegerField()
    room_pass = forms.CharField()
    max_player = forms.IntegerField()
    fee = forms.IntegerField()
    p1 = forms.IntegerField()
    p2 = forms.IntegerField()
    p3 = forms.IntegerField()
    p4 = forms.IntegerField()
    p5 = forms.IntegerField()
    p6 = forms.IntegerField()
    start_at = forms.DateTimeField()
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget = forms.PasswordInput)
    
class player(forms.Form):
    pubg_id = forms.CharField(max_length=20)
    

class money(forms.Form):
    trans_id = forms.CharField(max_length=20)
    payment = forms.IntegerField()

class setwinner(forms.Form):
    tournament_id = forms.IntegerField()
    pubg_id = forms.CharField(max_length=20)
    position = forms.IntegerField()
    
class join(forms.Form):
    tournament_id = forms.IntegerField()
    
class status(forms.Form):
    tournament_id = forms.IntegerField()
    status = forms.IntegerField()
    
    