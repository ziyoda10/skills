


# class AcceptMatchView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, match_id):
#         match = get_object_or_404(Match, id=match_id)

#         # Faqat qabul qiluvchi qabul qila oladi
#         if match.receiver != request.user:
#             return Response({"error": "Bu matchni qabul qilish huquqingiz yo'q"}, status=403)

#         if match.status != 'pending':
#             return Response({"error": "Bu match allaqachon ko'rib chiqilgan"}, status=400)

#         # Matchni qabul qilish
#         match.status = 'accepted'
#         match.save()

#         # Avtomatik Session yaratish
#         session = Session.objects.create(
#             skill=match.skill,
#             status='active'
#         )
#         session.users.add(match.sender, match.receiver)

#         return Response({
#             "message": "Match qabul qilindi va session yaratildi",
#             "session_id": session.id,
#             "skill": match.skill.name if hasattr(match.skill, 'name') else str(match.skill)
#         }, status=status.HTTP_200_OK)

# match/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Match
from skills_sessions.models import Session


class MatchSuggestionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # User o'rganmoqchi bo'lgan skill'larni topamiz
        my_learn_skills = user.userskill_set.filter(type='learn').values_list('skill_id', flat=True)

        suggestions = user.__class__.objects.filter(
            userskill__skill_id__in=my_learn_skills,
            userskill__type='offer'
        ).exclude(id=user.id).distinct()[:10]

        data = [{"id": u.id, "username": u.username} for u in suggestions]
        return Response(data)


class SendMatchRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        to_user_id = request.data.get('to_user')
        skill_id = request.data.get('skill')

        if not to_user_id or not skill_id:
            return Response({"error": "to_user va skill majburiy"}, status=400)

        match = Match.objects.create(
            sender=request.user,
            receiver_id=to_user_id,
            skill_id=skill_id
        )

        return Response({
            "message": "Match so'rovi yuborildi",
            "match_id": match.id
        }, status=status.HTTP_201_CREATED)


class AcceptMatchView(APIView):
    """Match qabul qilinganda Session avtomatik yaratiladi"""
    permission_classes = [IsAuthenticated]

    def post(self, request, match_id):
        match = get_object_or_404(Match, id=match_id)

        # Faqat qabul qiluvchi qabul qila oladi
        if match.receiver != request.user:
            return Response({"error": "Bu matchni qabul qilish huquqingiz yo'q"}, status=403)

        if match.status != 'pending':
            return Response({"error": "Bu match allaqachon ko'rib chiqilgan"}, status=400)

        # Matchni accepted qilish
        match.status = 'accepted'
        match.save()

        # Avtomatik Session yaratish
        session = Session.objects.create(
            skill=match.skill,
            status='active'
        )
        session.users.add(match.sender, match.receiver)

        return Response({
            "message": "Match muvaffaqiyatli qabul qilindi!",
            "session_id": session.id,
            "skill": getattr(match.skill, 'name', str(match.skill))
        }, status=status.HTTP_200_OK)