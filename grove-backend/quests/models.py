from django.db import models
from users.models import User
from django.contrib.admin import register
from django.contrib import admin

import random


class Quest(models.Model):
    decription = models.CharField(max_length=1024)
    status = models.BooleanField()
    user_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_to")
    user_from = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_from")
    exp = models.IntegerField(default=0)
    
    notification = None

    def request_quest(self, user_from: User):
        groves = user_from.get_groves()
        friends = list(
            map(
                lambda grove: grove.user_b if grove.user_a.id == self.id
                else grove.user_a,
                groves
            )
        )
        tree = random.choice(friends)
        prompts = ["Show me a tree!", "What are you eating?", "Make a sandwich",
                   "What's the weather like?", "How's your day?", "Show me something cute",
                   "Go for a walk", "Send a selfie!", "Go out to eat",
                   "What is todays fit?", "Where are you right now?", "Play a game with me!"]
        quest_prompt = random.choice(prompts)
        return Quest(
            description=quest_prompt,
            status=False,
            user_to=tree, 
            user_from=self,
            exp=10
        )
    def poke(self, user_from: User, user_to: User):
        poke = user_from + " poked you!"
        return Quest(
            description=poke,
            status=False,
            user_to= user_to, 
            user_from=self,
            exp=0
        )
        


@register(Quest)
class QuestAdmin(admin.ModelAdmin):
    pass
