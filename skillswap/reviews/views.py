from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from .models import Rating
from skills_sessions.models import Session

class GiveRatingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session_id = request.data.get('session')
        to_user_id = request.data.get('to_user')
        stars = request.data.get('stars')
        comment = request.data.get('comment', '')

        if not all([session_id, to_user_id, stars]):
            return Response({"error": "session, to_user va stars majburiy"}, status=400)

        if not (1 <= int(stars) <= 5):
            return Response({"error": "Stars 1 dan 5 gacha bo'lishi kerak"}, status=400)

        session = Session.objects.filter(id=session_id, users=request.user).first()
        if not session:
            return Response({"error": "Session topilmadi"}, status=404)

        rating, created = Rating.objects.get_or_create(
            session=session,
            from_user=request.user,
            to_user_id=to_user_id,
            defaults={'stars': stars, 'comment': comment}
        )

        if not created:
            return Response({"error": "Allaqachon baho bergansiz"}, status=400)

        return Response({"message": "Baho berildi! ⭐", "stars": rating.stars})


class UserRatingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        avg = Rating.objects.filter(to_user_id=user_id).aggregate(Avg('stars'))
        return Response({
            "user_id": user_id,
            "average_rating": round(avg['stars__avg'] or 0, 1)
        })
# Create your views here.
