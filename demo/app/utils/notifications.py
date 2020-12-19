import channels.layers
from asgiref.sync import async_to_sync
from django.db.models import TextChoices


class EventType(TextChoices):
    SERVER_STOP = 'server_stop'
    HIGHLIGHT_ITEMS = 'highlight_items'


def broadcast_event(event_type: EventType, payload: dict = None):
    channel_layer = channels.layers.get_channel_layer()
    message = {
        'type': 'broadcast_event',
        'message': {
            'event_type': event_type,
            'payload': payload,
        },
    }
    async_to_sync(channel_layer.group_send)('events', message)


def get_events_listeners_count():
    """Получить количество слушателей событий."""
    channel_layer = channels.layers.get_channel_layer()
    chs = channel_layer.groups.get('events')
    return len(chs) if chs else 0
