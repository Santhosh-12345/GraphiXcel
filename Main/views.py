from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import graphGen

def Main(request):
    requestDict=dict(request.POST.items())
    if request.method=='POST' and ('xaxis' in requestDict or 'yaxis' in requestDict or 'column' in requestDict):
        print(requestDict['graph'])
        if requestDict['graph']=="bar":
            graphGen.generate_bar_chart(requestDict['file'],requestDict['xaxis'],requestDict['yaxis'])
        elif requestDict['graph']=="line":
            graphGen.plot_with_matplotlib(requestDict['file'],requestDict['xaxis'],requestDict['yaxis'])
        elif requestDict['graph']=="pie":
            graphGen.generate_pie_chart(requestDict['file'],requestDict['column'])
        list=graphGen.getDataList(requestDict['file'])
        return render(request,'index.html',{'output':'true','file':requestDict['file'],'columns':list})
    elif request.method=='POST':
        print(dict(request.POST.items()))
        file=request.FILES['file']
        fileStorageSystem=FileSystemStorage()
        fileStorageSystem.save(file.name,file)
        list=graphGen.getDataList(file.name)
        return render(request,'index.html',{'columns':list,'file':file.name})
    return render(request,'index.html')