from django.shortcuts import render
import re


operations = {"Capitalize Text": str.upper, 
              "Remove Punctuations": lambda a: re.sub(r'[^\w\s]', '', a),
              "Remove Newline": lambda a: a.replace('\n', '').replace('\r', ''),
              "Remove Space": lambda a: a.replace(' ', ''),
              "Count Characters": len,
              "": str}

def home(request):
    return render(request, 'home.html')

def analyze(request):
    text = request.POST.get("text", "Default Value")
    operation = [request.POST.get("caps", ""), 
                 request.POST.get("removepunc", ""), 
                 request.POST.get("newlineremove", ""), 
                 request.POST.get("spaceremover", ""),
                 request.POST.get("countchars", "") ]
    for op in operation:
        if op == "Count Characters":
            text = f"{text} Char Count = {operations[op](text)}"
        else:  
            text = operations[op](text) 
    params = {"output": text, "operation": ",".join(operation)}
    return render(request, 'analyze.html', params)

def aboutus(request):
    return render(request, 'AboutUs.html')

def contactus(request):
    return render(request, 'ContactUs.html')