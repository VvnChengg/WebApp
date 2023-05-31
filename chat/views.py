# chat/views.py
from django.shortcuts import render
from chat.models import Message, Room
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def index(request):
    return render(request, "chat/index.html")


@login_required
def room(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        profile_himself = Profile.objects.get(user=request.user)
        messages_received = Message.objects.filter(sender=profile, receiver=profile_himself)
        messages_sent = Message.objects.filter(sender=profile_himself, receiver=profile)

        all_messages = messages_received | messages_sent    # collect all messages
        all_messages = all_messages.order_by('created_at')  # ordered by timestamp
        
        

    except User.DoesNotExist:
        print('User does not exist')
        return False
    except Profile.DoesNotExist:
        print('Profile does not exist')
        return False

    context = {
        'messages': all_messages,
        'user': request.user,
        'contact': profile,
        'room_name': username
    }
    return render(request, "chat/room.html", context)


def send_message(request, contact):
    if request.method == "POST":
        for i in range(5):
            print(contact)
        return HttpResponseRedirect(reverse("room", args=(contact, )))
