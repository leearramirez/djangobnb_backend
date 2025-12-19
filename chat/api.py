from django.http import JsonResponse


from rest_framework.decorators import api_view


from .models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer, ConversationDetailSerializer


from useraccount.models import User




@api_view(['GET'])
def conversations_list(request):
    serializer = ConversationListSerializer(request.user.conversations.all(), many=True)


    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conversation_detail(request, pk):
    try:
        conversation = request.user.conversations.get(pk=pk)

        conversation_serializer = ConversationDetailSerializer(conversation, many=False)

        return JsonResponse({
            'conversation': conversation_serializer.data,
        }, safe=False)
    except Conversation.DoesNotExist:
        return JsonResponse({'error': 'Conversation not found'}, status=404)