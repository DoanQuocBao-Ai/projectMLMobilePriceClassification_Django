from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
from .code import clz
import pickle
from .models import Clz

# Create your views here.
def index(request):
    return render(request, 'index.html')

def train(request):
    return render(request, 'train.html')

def predict(request):
    data = Clz.objects.all()
    return render(request, 'predict.html' ,{'data':data})

def tresult(request):
    if request.method == 'POST':     
        f = request.FILES['file']        
        mname = str(f)   
        c1 = clz.Clazif()
        acc = c1.train(f)

        #dump to database
        data = { 'model' : c1.classifier, 'scaler' : c1.sc, }
        bdata = pickle.dumps(data)
        t = Clz(name = mname, file = bdata, score = f"{acc*100:.2f}")
        t.save()
        result = f"{acc*100:.2f} %"
        return render(request, 'tresult.html' , {'accuracy': result})
    else:
        return HttpResponse("Hello World")
def presult(request):
    # if request.method == 'POST':

    mn = request.GET['name_of_select']
        
    vals = request.GET['val']
    vals = vals.split()
    vals = list(map(float,vals))

        #load from data base
    data = Clz.objects.all()
    for m in data:
        if m.name == mn:
            model = pickle.loads(m.file)
    X = model['scaler'].transform([vals])
    y = model['model'].predict(X)
    return render(request, 'presult.html' ,{'values':y})
def database(request):
    db = Clz.objects.all()
    return render(request, 'database.html' ,{'db':db})