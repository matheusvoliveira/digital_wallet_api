# from rest_framework import generics
# from .models import Usuario
# from .serializers import UsuarioSerializer

# class UsuarioListCreateView(generics.ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer




# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate
# from rest_framework.permissions import IsAuthenticated
# from .models import Usuario
# from .serializers import UsuarioSerializer

# # Criar usuário
# class UsuarioCreateView(generics.CreateAPIView):

#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # Login com JWT
# class LoginView(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(email=email, password=password)
#         try:
#             user = Usuario.objects.get(email=email)  # Buscar usuário pelo email
#         except Usuario.DoesNotExist:
#             return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

#         if not user.check_password(password):  # Verifica a senha
#             return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#             })
#         return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

# # Rota protegida para testar autenticação
# class ProtectedView(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "Você está autenticado!"}, status=status.HTTP_200_OK)



# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated
# from .models import Usuario, Wallet
# from .serializers import UsuarioSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView


# # Criar usuário (sem listar usuários)
# class UsuarioCreateView(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # Login com JWT
# class LoginView(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         try:
#             user = Usuario.objects.get(email=email)
#         except Usuario.DoesNotExist:
#             return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

#         if not user.check_password(password):
#             return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(user)
#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "user": {  # Adicionando os dados do usuário na resposta
#                 "id": user.id,
#                 "nome": user.nome,
#                 "email": user.email
#             }
#         })
        
        
# class UsuarioDetailView(generics.RetrieveAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         user = request.user
#         return Response({
#             "id": user.id,
#             "nome": user.nome,
#             "email": user.email
#         })


# # Rota protegida para testar autenticação
# class ProtectedView(generics.GenericAPIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "Você está autenticado!"}, status=status.HTTP_200_OK)

# class CustomTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
        
#         # Obtém o usuário autenticado
#         user = request.user  # Pegamos o usuário autenticado no request

#         # Adiciona a mensagem e o nome do usuário na resposta
#         response.data['user'] = {
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "email": user.email
#         }

#         return response
    
    
# class TransferenciaView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         remetente = request.user
#         destinatario_email = request.data.get("destinatario")
#         valor = request.data.get("valor")

#         if not destinatario_email or not valor:
#             return Response({"erro": "Destinatário e valor são obrigatórios."}, status=400)

#         try:
#             valor = float(valor)
#         except ValueError:
#             return Response({"erro": "Valor inválido."}, status=400)

#         destinatario = get_object_or_404(Usuario, email=destinatario_email)

#         # Obtém as carteiras do remetente e do destinatário
#         carteira_remetente = get_object_or_404(Wallet, usuario=remetente)
#         carteira_destinatario = get_object_or_404(Wallet, usuario=destinatario)

#         try:
#             carteira_remetente.transferir(carteira_destinatario, valor)
#             return Response({"mensagem": "Transferência realizada com sucesso!"})
#         except Exception as e:
#             return Response({"erro": str(e)}, status=400)








# from django.shortcuts import get_object_or_404
# from rest_framework import generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import Usuario, Wallet
# from .serializers import UsuarioSerializer

# # Criar usuário
# class UsuarioCreateView(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # Login com JWT
# class LoginView(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         try:
#             user = Usuario.objects.get(email=email)
#         except Usuario.DoesNotExist:
#             return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

#         if not user.check_password(password):
#             return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(user)
#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "user": {
#                 "id": user.id,
#                 "nome": user.nome,
#                 "email": user.email
#             }
#         })

# # Detalhes do usuário logado
# class UsuarioDetailView(generics.RetrieveAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         user = request.user
#         return Response({
#             "id": user.id,
#             "nome": user.nome,
#             "email": user.email
#         })

# # Transferência de dinheiro entre usuários autenticados
# class TransferenciaView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         remetente = request.user
#         destinatario_email = request.data.get("destinatario")
#         valor = request.data.get("valor")

#         if not destinatario_email or not valor:
#             return Response({"erro": "Destinatário e valor são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             valor = float(valor)
#         except ValueError:
#             return Response({"erro": "Valor inválido."}, status=status.HTTP_400_BAD_REQUEST)

#         destinatario = get_object_or_404(Usuario, email=destinatario_email)
#         carteira_remetente = get_object_or_404(Wallet, usuario=remetente)
#         carteira_destinatario = get_object_or_404(Wallet, usuario=destinatario)

#         try:
#             carteira_remetente.transferir(carteira_destinatario, valor)
#             return Response({"mensagem": "Transferência realizada com sucesso!"})
#         except Exception as e:
#             return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# # Depósito de dinheiro para qualquer usuário (não precisa de login)
# class DepositoView(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         valor = request.data.get("valor")

#         if not email or not valor:
#             return Response({"erro": "Email e valor são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             valor = float(valor)
#         except ValueError:
#             return Response({"erro": "Valor inválido."}, status=status.HTTP_400_BAD_REQUEST)

#         usuario = get_object_or_404(Usuario, email=email)
#         carteira = get_object_or_404(Wallet, usuario=usuario)

#         try:
#             carteira.adicionar_saldo(valor)
#             return Response({"mensagem": f"Depósito de R$ {valor:.2f} realizado para {email}."}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)









# from django.shortcuts import get_object_or_404
# from rest_framework import generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import Usuario
# from .serializers import UsuarioSerializer

# # Criar usuário (já cria a Wallet automaticamente)
# class UsuarioCreateView(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # Login com JWT
# class LoginView(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         try:
#             user = Usuario.objects.get(email=email)
#         except Usuario.DoesNotExist:
#             return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

#         if not user.check_password(password):
#             return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(user)
#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "user": {
#                 "id": user.id,
#                 "nome": user.nome,
#                 "email": user.email
#             }
#         })

# # Detalhes do usuário logado
# class UsuarioDetailView(generics.RetrieveAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         user = request.user
#         return Response({
#             "id": user.id,
#             "nome": user.nome,
#             "email": user.email
#         })

# # Transferência de dinheiro entre usuários autenticados
# class TransferenciaView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         remetente = request.user
#         destinatario_email = request.data.get("destinatario")
#         valor = request.data.get("valor")

#         if not destinatario_email or not valor:
#             return Response({"erro": "Destinatário e valor são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             valor = float(valor)
#             if valor <= 0:
#                 raise ValueError
#         except ValueError:
#             return Response({"erro": "Valor inválido."}, status=status.HTTP_400_BAD_REQUEST)

#         destinatario = get_object_or_404(Usuario, email=destinatario_email)

#         carteira_remetente = get_object_or_404(Wallet, usuario=remetente)
#         carteira_destinatario = get_object_or_404(Wallet, usuario=destinatario)

#         if carteira_remetente.saldo < valor:
#             return Response({"erro": "Saldo insuficiente."}, status=status.HTTP_400_BAD_REQUEST)

#         carteira_remetente.saldo -= valor
#         carteira_remetente.save()

#         carteira_destinatario.saldo += valor
#         carteira_destinatario.save()

#         return Response({"mensagem": "Transferência realizada com sucesso!"}, status=status.HTTP_200_OK)

# # Depósito de dinheiro para qualquer usuário (não precisa de login)
# class DepositoView(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         valor = request.data.get("valor")

#         if not email or not valor:
#             return Response({"erro": "Email e valor são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             valor = float(valor)
#         except ValueError:
#             return Response({"erro": "Valor inválido."}, status=status.HTTP_400_BAD_REQUEST)

#         usuario = get_object_or_404(Usuario, email=email)
#         carteira = get_object_or_404(Wallet, usuario=usuario)

#         try:
#             carteira.adicionar_saldo(valor)
#             return Response({"mensagem": f"Depósito de R$ {valor:.2f} realizado para {email}."}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)






# from django.shortcuts import get_object_or_404
# from rest_framework import generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import Usuario, Wallet
# from .serializers import UsuarioSerializer

# # Criar usuário (já cria a Wallet automaticamente)
# class UsuarioCreateView(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # Login com JWT
# class LoginView(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         usuario = get_object_or_404(Usuario, email=email)

#         if not usuario.check_password(password):
#             return Response({"erro": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(usuario)
#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "usuario": {
#                 "id": usuario.id,
#                 "nome": usuario.nome,
#                 "email": usuario.email
#             }
#         })

# # Detalhes do usuário autenticado
# class UsuarioDetailView(generics.RetrieveAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         usuario = request.user
#         return Response({
#             "id": usuario.id,
#             "nome": usuario.nome,
#             "email": usuario.email
#         })



# from django.shortcuts import get_object_or_404
# from rest_framework import generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import Usuario
# from .serializers import UsuarioSerializer

# # Criar usuário
# class UsuarioCreateView(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# # Login com JWT
# class LoginView(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         usuario = get_object_or_404(Usuario, email=email)

#         if not usuario.check_password(password):
#             return Response({"erro": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(usuario)
#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "usuario": {
#                 "id": usuario.id,
#                 "nome": usuario.nome,
#                 "email": usuario.email
#             }
#         })

# # Detalhes do usuário autenticado
# class UsuarioDetailView(generics.RetrieveAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         usuario = request.user
#         return Response({
#             "id": usuario.id,
#             "nome": usuario.nome,
#             "email": usuario.email
#         })

# # Transferência de saldo removida, pois depende do Wallet


# from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.shortcuts import get_object_or_404
# from .models import Usuario
# from .serializers import UsuarioSerializer
# from django.db import transaction



# # Criar usuário
# class UsuarioCreateView(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer


# # Login com JWT
# class LoginView(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         usuario = get_object_or_404(Usuario, email=email)

#         if not usuario.check_password(password):
#             return Response({"erro": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(usuario)
#         return Response({
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#             "usuario": {
#                 "id": usuario.id,
#                 "nome": usuario.nome,
#                 "email": usuario.email,
#                 "saldo": usuario.saldo  # Incluindo saldo na resposta do login
#             }
#         })


# # Detalhes do usuário autenticado
# class UsuarioDetailView(generics.RetrieveAPIView):
#     serializer_class = UsuarioSerializer
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         usuario = request.user
#         return Response({
#             "id": usuario.id,
#             "nome": usuario.nome,
#             "email": usuario.email,
#             "saldo": usuario.saldo  # Incluindo saldo
#         })


# # Listar todos os usuários
# class ListaUsuariosView(generics.ListAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     # permission_classes = [IsAuthenticated]  # Somente usuários autenticados podem ver


# # Atualizar saldo do usuário autenticado
# @api_view(["PATCH"])
# @permission_classes([IsAuthenticated])
# def atualizar_saldo(request, pk):
#     usuario = get_object_or_404(Usuario, id=pk)

#     # Verifica se o usuário logado está tentando atualizar seu próprio saldo
#     if request.user != usuario:
#         return Response({"erro": "Você não tem permissão para alterar este saldo."}, status=status.HTTP_403_FORBIDDEN)

#     aumento = request.data.get("aumento", 0)
    
#     try:
#         aumento = float(aumento)
#     except ValueError:
#         return Response({"erro": "O valor do aumento deve ser um número válido."}, status=status.HTTP_400_BAD_REQUEST)

#     usuario.saldo += aumento
#     usuario.save()

#     return Response({
#         "mensagem": f"Saldo atualizado: R$ {usuario.saldo}",
#         "novo_saldo": usuario.saldo
#     }, status=status.HTTP_200_OK)



# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def transferir_saldo(request):
#     remetente = request.user
#     destinatario_id = request.data.get("destinatario_id")
#     valor = request.data.get("valor")

#     # Validação do valor
#     try:
#         valor = float(valor)
#         if valor <= 0:
#             return Response({"erro": "O valor da transferência deve ser maior que zero."}, status=status.HTTP_400_BAD_REQUEST)
#     except ValueError:
#         return Response({"erro": "O valor deve ser um número válido."}, status=status.HTTP_400_BAD_REQUEST)

#     # Verificar se o usuário tem saldo suficiente
#     if remetente.saldo < valor:
#         return Response({"erro": "Saldo insuficiente."}, status=status.HTTP_400_BAD_REQUEST)

#     # Buscar destinatário
#     destinatario = get_object_or_404(Usuario, id=destinatario_id)

#     # Evitar transferência para si mesmo
#     if remetente == destinatario:
#         return Response({"erro": "Você não pode transferir para si mesmo."}, status=status.HTTP_400_BAD_REQUEST)

#     # Realizar transferência
#     with transaction.atomic():
#         remetente.saldo -= valor
#         destinatario.saldo += valor
#         remetente.save()
#         destinatario.save()

#     return Response({
#         "mensagem": "Transferência realizada com sucesso!",
#         "novo_saldo": remetente.saldo
#     }, status=status.HTTP_200_OK)




from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import Usuario
from .serializers import UsuarioSerializer

# Criar usuário
class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Login com JWT
class LoginView(generics.GenericAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        usuario = get_object_or_404(Usuario, email=email)

        if not usuario.check_password(password):
            return Response({"erro": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(usuario)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "usuario": {
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                "saldo": usuario.saldo
            }
        })

# Detalhes do usuário autenticado
class UsuarioDetailView(generics.RetrieveAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        usuario = request.user
        return Response({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "saldo": usuario.saldo
        })

# Listar todos os usuários
class ListaUsuariosView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated]

# Atualizar saldo do próprio usuário
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def atualizar_saldo(request, pk):
    usuario = get_object_or_404(Usuario, id=pk)

    if request.user != usuario:
        return Response({"erro": "Você não tem permissão para alterar este saldo."}, status=status.HTTP_403_FORBIDDEN)

    aumento = request.data.get("aumento", 0)

    try:
        aumento = float(aumento)
    except ValueError:
        return Response({"erro": "O valor do aumento deve ser um número válido."}, status=status.HTTP_400_BAD_REQUEST)

    usuario.saldo += aumento
    usuario.save()

    return Response({
        "mensagem": f"Saldo atualizado: R$ {usuario.saldo}",
        "novo_saldo": usuario.saldo
    }, status=status.HTTP_200_OK)

# Transferência de saldo entre usuários
@api_view(["POST"])
def transferir_saldo(request):
    remetente_id = request.data.get("remetente_id")
    destinatario_id = request.data.get("destinatario_id")
    valor = request.data.get("valor")

    if not remetente_id or not destinatario_id:
        return Response({"erro": "IDs de remetente e destinatário são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        valor = float(valor)
        if valor <= 0:
            return Response({"erro": "O valor da transferência deve ser maior que zero."}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({"erro": "O valor deve ser um número válido."}, status=status.HTTP_400_BAD_REQUEST)

    # Busca usuários
    remetente = get_object_or_404(Usuario, id=remetente_id)
    destinatario = get_object_or_404(Usuario, id=destinatario_id)

    if remetente == destinatario:
        return Response({"erro": "Você não pode transferir para si mesmo."}, status=status.HTTP_400_BAD_REQUEST)

    if remetente.saldo < valor:
        return Response({"erro": "Saldo insuficiente."}, status=status.HTTP_400_BAD_REQUEST)

    with transaction.atomic():
        remetente.saldo -= valor
        destinatario.saldo += valor
        remetente.save()
        destinatario.save()

    return Response({
        "mensagem": "Transferência realizada com sucesso!",
        "novo_saldo": remetente.saldo
    }, status=status.HTTP_200_OK)
