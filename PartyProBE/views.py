from rest_framework import status, generics
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from .models import GuestRSVP, FoodItem, Catering
from rest_framework.permissions import AllowAny


# @csrf_exempt


@api_view(['GET', 'POST'])
def guest_list(request):
    # Retrieve or update the guest list.
    if request.method == 'GET':
        guest_list = GuestRSVP.objects.all()
        serializer = GuestRSVPSerializer(guest_list, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = GuestRSVPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def guest_detail(request, rsvp_id):
    # Retrieve, update, or delete a guest RSVP instance.
    try:
        guest = GuestRSVP.objects.get(rsvp_id=rsvp_id)
    except GuestRSVP.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestRSVPSerializer(guest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GuestRSVPSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def food_list(request):
    # Retrieve or update the food list.
    if request.method == 'GET':
        food_list = FoodItem.objects.all()
        serializer = FoodItemSerializer(food_list, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = FoodItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def food_detail(request, rsvp_id):
    # Retrieve, update, or delete food instance.
    try:
        food = FoodItem.objects.get(rsvp_id=rsvp_id)
    except FoodItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodItemSerializer(food)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodItemSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def catering_list(request):
    # Retrieve or update the food list.
    if request.method == 'GET':
        catering_list = Catering.objects.all()
        serializer = CateringSerializer(catering_list, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = CateringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Catering_detail(request, rsvp_id):
    # Retrieve, update, or delete food instance.
    try:
        Catering_detail = Catering.objects.get(rsvp_id=rsvp_id)
    except Catering.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CateringSerializer(Catering_detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CateringSerializer(Catering_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Catering_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def event_list(request):
    # Retrieve or update the food list.
    if request.method == 'GET':
        event_list = Event.objects.all()
        serializer = CateringSerializer(event_list, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Event_detail(request, rsvp_id):
    # Retrieve, update, or delete food instance.
    try:
        Event_detail = Event.objects.get(rsvp_id=rsvp_id)
    except Catering.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(Event_detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer(Event_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Event_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def guest_list(request):
#     #Retrieve or update the customer list.
#     if request.method == 'GET':
#         guests = GuestRSVP.objects.all()
#         serializer = GuestRSVPSerializer(guests, context={'request': request}, many=True)
#         return Response({'data': serializer.data})
#
#     elif request.method == 'POST':
#         serializer = GuestRSVPSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'POST'])
# def guest_list(request):
#     if request.method == 'GET':
#         customers = GuestRSVP.objects.all()
#         serializer = GuestRSVPSerializer(customers, context={'request': request}, many=True)
#         return Response({'data': serializer.data})
#
#     elif request.method == 'POST':
#         #if agent not specified, set the user id of the person requesting the new customer
#         # as the agent for this customer
#         if 'agent' not in request.data.keys():
#             request.data['agent'] = request.user.id
#
#         serializer = GuestRSVPSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def getCustomer(request, pk):
#     #Retrieve, update or delete a customer instance.
#     try:
#         customer = Customer.objects.get(pk=pk)
#     except Customer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CustomerSerializer(customer,context={'request': request})
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CustomerSerializer(customer, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def investment_list(request):
#     #Retrieve or update the investment list.
#     if request.method == 'GET':
#         investment = Investment.objects.all()
#         serializer = InvestmentSerializer(investment, context={'request': request}, many=True)
#         return Response({'data': serializer.data})
#
#     elif request.method == 'POST':
#         serializer = InvestmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PUT', 'DELETE'])
# def getInvestment(request, pk):
#     #Retrieve, update or delete an investment instance.
#     try:
#         investment = Investment.objects.get(pk=pk)
#     except Investment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = InvestmentSerializer(investment, context={'request': request})
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = InvestmentSerializer(investment, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         investment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def stock_list(request):
#     #Retrieve or update the stock list.
#     if request.method == 'GET':
#         stock = Stock.objects.all()
#         serializer = StockSerializer(stock, context={'request': request}, many=True)
#         return Response({'data': serializer.data})
#
#     elif request.method == 'POST':
#         serializer = StockSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def getStock(request, pk):
#      # Retrieve, update or delete a stock instance.
#     try:
#         stock = Stock.objects.get(pk=pk)
#     except Stock.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = StockSerializer(stock,context={'request': request})
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = StockSerializer(stock, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         stock.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class RegisterView(generics.CreateAPIView):
#     #Register a new user - requester need not be authorized
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer
#
# @api_view(['GET', 'POST'])
# def my_customer_list(request):
#     if request.method == 'GET':
#         customers = Customer.objects.filter(agent=request.user)
#         serializer = CustomerSerializer(customers, context={'request': request}, many=True)
#         return Response({'data': serializer.data})
#
#     elif request.method == 'POST':
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET'])
# def getUser(request):
#     #Request the information about the user making the request
#     try:
#         user = User.objects.get(pk=request.user.id)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user, context={'request': request})
#         return Response(serializer.data)
