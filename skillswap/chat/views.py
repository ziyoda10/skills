# chat/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message
from skills_sessions.models import Session

class SessionMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, session_id):
        session = Session.objects.filter(id=session_id, users=request.user).first()
        if not session:
            return Response({"error": "Session topilmadi yoki sizga tegishli emas"}, status=403)

        messages = Message.objects.filter(session=session)
        data = [
            {
                "id": m.id,
                "sender": m.sender.username,
                "text": m.text,
                "created_at": m.created_at
            } 
            for m in messages
        ]
        return Response(data)

    def post(self, request, session_id):
        session = Session.objects.filter(id=session_id, users=request.user).first()
        if not session:
            return Response({"error": "Session topilmadi"}, status=403)

        text = request.data.get('text')
        if not text:
            return Response({"error": "text maydoni bo'sh bo'lmasligi kerak"}, status=400)

        message = Message.objects.create(
            session=session,
            sender=request.user,
            text=text
        )

        return Response({
            "message": "Xabar yuborildi",
            "data": {
                "id": message.id,
                "sender": message.sender.username,
                "text": message.text
            }
        })
