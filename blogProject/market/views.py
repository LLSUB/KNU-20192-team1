from django.shortcuts import render, get_object_or_404, redirect
from .models import Market, Menu
from django.contrib.auth.models import User

# Create your views here.
def market(request):
    markets = Market.objects 
    market_list = Market.objects.all().order_by('-id') # 블로그 객체 최신순나열
    #paginator = Paginator(board_list, 2) # 3개씩 잘라내기
    #page = request.GET.get('page') # 페이지 번호 알아오기
    #posts = paginator.get_page(page) # 페이지 번호 인자로 넘겨주기
    return render(request, 'market.html', {'markets':market_list})

def detail(request, market_id):
    market_detail=get_object_or_404(Market, pk=market_id)

    user=request.user
    if market_detail.likes.filter(id=user.id):
        message="즐겨찾기 취소"
    else:
        message="즐겨찾기 등록"

    return render(request, 'detail.html',{'market':market_detail, 'message':message})

def new(request):
    return render(request, 'new.html')

def order(request, market_id):
    market_detail=get_object_or_404(Market, pk=market_id)
    return render(request, 'order.html',{'market':market_detail})

def create(request):
    market=Market()
    market.name=request.GET['name']
    market.address=request.GET['address']
    market.start_time=request.GET['start_time']
    market.end_time=request.GET['end_time']
    market.description=request.GET['description']
    #market.user=get_object_or_404(User, pk=request.GET['user_id'])
    market.save()

    return redirect('/market/'+str(market.id))


def menu_create(request, market_id):
    menu=Menu() # menu를 저장하기 위해 빈 Menu 객체를 하나 생성
    #menu.name=request.POST['name'] # 댓글의 내용을 받아옴
    menu.photo=request.FILES['photo']
    menu.price=request.POST['price']
    menu.left=request.POST['left']
    menu.description=request.POST['description']
    menu.market=get_object_or_404(Market, pk=market_id) # 해당 댓글을 어떤 blog 객체와 연결시켜 줄 것인지 찾아온다
    menu.save() # comment를 DB에 저장
    return redirect('/market/'+str(market_id))

def post_like(request, market_id):
    user = request.user # 로그인된 유저의 객체를 가져온다.
    market = get_object_or_404(Market, pk=market_id) # 좋아요 버튼을 누를 글을 가져온다.

    # 이미 좋아요를 눌렀다면 좋아요를 취소, 아직 안눌렀으면 좋아요를 누른다.
    if market.likes.filter(id=user.id): # 로그인한 user가 현재 blog 객체에 좋아요를 눌렀다면
        market.likes.remove(user) # 해당 좋아요를 없앤다.
    else: # 아직 좋아요를 누르지 않았다면
        market.likes.add(user) # 좋아요를 추가한다.

    return redirect('/market/' + str(market_id)) # 좋아요 처리를 하고 detail 페이지로 간다.

def delete(request, market_id):
    market=get_object_or_404(Market, pk=market_id)
    market.delete()

    return redirect('market')

def market_search(request):
    market=Market.objects.all()

    m=request.GET.get('context','init')

    if m:
        market=market.filter(name__icontains=m)
    
    return render(request, 'market_search.html', {
        'market_search': market,
        'm':m,
    })

