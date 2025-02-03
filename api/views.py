from rest_framework import generics, permissions
from .models import User, PlantCategory, Plant
from .serializers import PlantCategorySerializer, PlantSerializer, UserLoginSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .permissions import IsAdminUser, IsFarmerUser, IsRegularUser
# User Views
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        # استخدام الـ Backend المخصص للتعامل مع phone_number
        user = authenticate(request, phone_number=phone_number, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
# PlantCategory Views
class PlantCategoryListCreateView(generics.ListCreateAPIView):
    queryset = PlantCategory.objects.all()
    serializer_class = PlantCategorySerializer
    permission_classes = [IsAdminUser]

class PlantCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantCategory.objects.all()
    serializer_class = PlantCategorySerializer
    permission_classes = [IsAdminUser]

# Plant Views
class PlantListCreateView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsFarmerUser]

class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsFarmerUser]


class CategoryListView(generics.ListAPIView):
    queryset = PlantCategory.objects.all()
    serializer_class = PlantCategorySerializer
    permission_classes = [IsRegularUser | IsFarmerUser | IsAdminUser]
        
        
class PlantListView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsRegularUser | IsFarmerUser | IsAdminUser]