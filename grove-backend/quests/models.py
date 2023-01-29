from django.db import models
from users.models import User
import random
# Create your models here.

class Quest(models.Model):
    decription = models.CharField(max_length=1024)
    status = models.BooleanField()
    user_to = models.ForeignKey(User, on_delete=models.CASCADE)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    exp = models.IntegerField(default=0)

def request_user(self, user_from: User):
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
    quest = random.choice(prompts)
    return quest