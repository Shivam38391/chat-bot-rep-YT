from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os
import time
import openai

# openai.Model.list()
# Create your views here.





# organisation key
openai.organization = "your organization key"
# api key
openai.api_key = "your api key"



def index(request):
    return render(request, "index.html")


def chatAPI(request):
    
    try:
        
        if request.method == "POST":
            prompt = request.POST["prompt"]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.5,
                max_tokens=20,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(type(response))
            return JsonResponse(response)
        
        
     # when response is not get from server   
    except:
        response = {"choices": [
    {

      "text": "\n\n I guess you are not connected to internet, please check your connectivity!"
    }
        ],
            "created": 1684271063,
            }
        
        
        return JsonResponse(response)

        
    return HttpResponse("Bad Request")


















# def index(request):
    
#     # model_engine = "text-davinci-003"
#     # prompt = "Hello, how can I assist you today?"
    
#     userMessages = []
#     botResponse= []


    
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         print(user_input)
#         userMessages.append(user_input)
#         print("usermesaage list:-", userMessages)
#         response = openai.Completion.create(engine="text-davinci-003", prompt=user_input,max_tokens=20,n=1,stop=None,temperature=0.5,)
        
#         message = response.choices[0].text.strip()
#         botResponse.append(message)
#         print(message)
#         print("bot response list:-", botResponse)
        
        
#         context = {
#             "usermessages": userMessages,
#             "botresponse": botResponse,
#         }
#         return render(request,"index.html",context)
#     else:
#         return render(request,"index.html")