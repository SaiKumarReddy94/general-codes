from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from collections import deque

ticket_options = [
    'Change oil',
    'Inflate tires',
    'diagnostic',
]
ticket_number = 0
next_ticket = 0
service_line = {"change_oil": [], "inflate_tires": [], "diagnostic": []}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h2>Welcome to the Hypercar Service!</h2>")


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 't_hcar/menu.html', context={'options': ticket_options})
    # def get(self, request, *args, **kwargs):
    #     return render(request, "t_hcar/menu.html")


class TicketView(View):
    def get(self, request, service, *args, **kwargs):
        if service == "change_oil":
            global wait_time
            wait_time = len(service_line["change_oil"]) * 2
        elif service == "inflate_tires":
            wait_time = len(service_line["change_oil"]) * 2 + len(service_line["inflate_tires"]) * 5
        elif service == "diagnostic":
            wait_time = len(service_line["change_oil"]) * 2 + len(service_line["inflate_tires"]) * 5 + len(
                service_line["diagnostic"] * 30)
        global ticket_number
        ticket_number += 1
        service_line[service].append(ticket_number)
        return render(request, 't_hcar/t_request.html', context={"ticket": ticket_number, "wait": wait_time})


class ProcessView(View):
    tickets = TicketView()

    def get(self, request, *args, **kwargs):
        return render(request, 't_hcar/processing.html', {"service_line": service_line})

    def post(self, request, *args, **kwargs):
        global next_ticket
        if len(service_line['change_oil']) > 0:
            next_ticket = service_line['change_oil'].pop(0)
        elif len(service_line['inflate_tires']) > 0:
            next_ticket = service_line['inflate_tires'].pop(0)
        elif len(service_line['diagnostic']) > 0:
            next_ticket = service_line['diagnostic'].pop(0)
        else:
            next_ticket = 0
        return redirect('/next')


class Next(View):
    def get(self, request, *args, **kwargs):
        return render(request, 't_hcar/next.html', {"next_ticket": next_ticket})
