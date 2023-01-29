from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view
from users.models import User
from groves.models import Grove
from challenge.models import UserChallenge, DailyChallenge, DailyChallengeCompletion
from challenge.serializers import UserChallengeSerializer, DailyChallengeSerializer
from notifications.models import Notification
import random


@api_view(["POST"])
def create_challenge(request):
    user = User.get_by_username(request.user)
    friends = Grove.get_friends(user)
    print(friends)
    challengee = random.choice(friends)
    prompts = [
        "Show me a tree!",
        "What are you eating?",
        "Make a sandwich",
        "What's the weather like?",
        "How's your day?",
        "Show me something cute",
        "Go for a walk",
        "Send a selfie!",
        "Go out to eat",
        "What is todays fit?",
        "Where are you right now?",
        "Play a game with me!",
    ]
    prompt = random.choice(prompts)
    chal = UserChallenge(desc=prompt, dst=challengee, src=user, xp=10)

    n = Notification(
        user_to=challengee,
        content=f"{prompt}",
        src=f"{user.first_name} {user.last_name}",
    )
    chal.save()
    n.save()
    return Response(UserChallengeSerializer(chal, many=False).data)


@api_view(["GET"])
def get_active_challenges(request):
    user = User.get_by_username(request.user)
    chals = UserChallenge.objects.filter(dst=user).all()
    completed_dailies = map(
        lambda c: c.daily, DailyChallengeCompletion.objects.filter(user=user).all()
    )
    dailies = DailyChallenge.objects.exclude(id__in=completed_dailies)
    all_chals = (
        UserChallengeSerializer(chals, many=True).data
        + DailyChallengeSerializer(dailies, many=True).data
    )
    return Response(all_chals)


@api_view(["DELETE"])
def complete_challenge(request):
    user = User.get_by_username(request.user)
    data = request.data
    if data["daily"]:
        chal = DailyChallenge.objects.filter(id=data["id"]).first()
        t = DailyChallengeCompletion(daily=chal, user=user)
        t.save()
        ser = DailyChallengeSerializer(chal).data
        return Response(ser)
    else:
        chal = UserChallenge.oobjects.filter(id=data["id"]).first()
        grove = Grove.get_grove(user, chal.src)
        grove.xp += chal.xp
        grove.save()
        ser = UserChallengeSerializer(chal).data
        chal.delete()
        return Response(ser)
