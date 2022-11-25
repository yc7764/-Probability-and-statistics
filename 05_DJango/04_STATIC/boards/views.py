from django.shortcuts import render, redirect

#추가
from . models import Board

# Create your views here.
def index(request):
    #boards = Board.objects.all()
    board_all = Board.objects.order_by('-pk')
    context={
        'boards':board_all
    }
    return render(request, "boards/index.html" , context)

def registerfrm(request):
    return render(request, "boards/registerfrm.html")


def register(request):
    title = request.POST.get('title')
    content= request.POST.get('content')
    
    #추가하기
    try:
        image = request.FILES['image']
    except:
        image = None
        
    board = Board(title=title, content = content, image = image)
    board.save()
    
    #templates가 아닌 url로 요청을 다시 보내는 랜더링 방법.. redirect
    #return render(request, "boards/register.html")
    return redirect('boards:index')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    
    context={
        'board':board
    }
    return render(request, "boards/detail.html" , context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)

    if request.method=="POST":
        board.delete()
        return redirect('boards:index')

    else:
        return redirect('boards:detail', board.pk)

def updatefrm(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board':board
    }

    return render(request, "boards/updatefrm.html", context)

def update(request, pk):
    board = Board.objects.get(pk=pk) #수정되기전
    
    #수정폼에 입력된 값을 아래서 받아온다...수정됨
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('boards:detail', pk)