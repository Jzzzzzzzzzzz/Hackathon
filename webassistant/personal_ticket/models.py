from django.db import models
from django.conf import settings  # Для ссылки на текущую модель пользователя
from assistant.models import Ticket





class Message(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Используем кастомную модель пользователя
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user.username} on {self.ticket.title}"