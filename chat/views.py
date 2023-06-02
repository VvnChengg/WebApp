# chat/views.py
from django.shortcuts import render
from chat.models import Message, Room, RoomDetail
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


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
        all_messages = all_messages.order_by(
            'created_at')  # ordered by timestamp

        # Check if room details already exist
        room_detail = RoomDetail.objects.filter(room_name=f"Room for {profile.user} and {profile_himself.user}").first()
        if not room_detail:
            room_detail = RoomDetail.objects.filter(room_name=f"Room for {profile_himself.user} and {profile.user}").first()

        if not room_detail:
            # Create new room details if it doesn't exist
            room_detail = RoomDetail.objects.create(
                room_name=f"Room for {profile.user} and {profile_himself.user}",
                room_description="No description yet.",
                room_capacity=2
            )
            room_detail.save()

            new_room_member = Room.objects.create(
                member=profile,
                room_detail=room_detail
            )
            new_room_member.save()
            new_room_himself = Room.objects.create(
                member=profile_himself,
                room_detail=room_detail
            )
            new_room_himself.save()

    except User.DoesNotExist:
        print('User does not exist')
        return render(request, "chat/index.html", {"alert": "No such user named: " + username})
    except Profile.DoesNotExist:
        print('Profile does not exist')
        return False

    rooms_himself = Room.objects.filter(member=profile_himself)
    room_details_himself = [room.room_detail for room in rooms_himself]

    other_rooms = Room.objects.filter(
        ~Q(member=profile_himself),  # Exclude rooms associated with Profile A
        room_detail__in=room_details_himself
    )

    context = {
        'messages': all_messages,
        'user': request.user,
        'contact': profile,
        'room_name': username,
        'rooms': other_rooms,
    }

    return render(request, "chat/room.html", context)


def send_message(request, contact):
    if request.method == "POST":
        return HttpResponseRedirect(reverse("room", args=(contact, )))
