from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer
from products.models import Item


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def wishlist(request, pk):
    profile = request.user.profile
    product = Item.objects.get(id=pk)
    if profile.wishlist.filter(id=product.id).exists():
        profile.wishlist.remove(product)
    else:
        profile.wishlist.add(product)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)