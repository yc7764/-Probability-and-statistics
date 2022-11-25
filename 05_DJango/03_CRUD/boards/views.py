import io
from PIL import Image as im
import torch

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import ImageModel
from .forms import ImageUploadForm

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
    
    board = Board(title=title, content = content)
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

class UploadImage(CreateView):
    model = ImageModel
    template_name = 'image/imagemodel_form.html'
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.get('image')
            img_instance = ImageModel(
                image=img
            )
            img_instance.save()

            uploaded_img_qs = ImageModel.objects.filter().last()
            img_bytes = uploaded_img_qs.image.read()
            img = im.open(io.BytesIO(img_bytes))

            # Change this to the correct path
            path_hubconfig = "hubconf.py"
            path_weightfile = "best.pt"  # or any custom trained model

            model = torch.hub.load(path_hubconfig, 'custom',
                               path=path_weightfile, source='local')

            results = model(img, size=640)
            results.render()
            for img in results.imgs:
                img_base64 = im.fromarray(img)
                img_base64.save("media/yolo_out/image0.jpg", format="JPEG")

            inference_img = "/media/yolo_out/image0.jpg"

            form = ImageUploadForm()
            context = {
                "form": form,
                "inference_img": inference_img
            }
            return render(request, 'image/imagemodel_form.html', context)

        else:
            form = ImageUploadForm()
        context = {
            "form": form
        }
        return render(request, 'image/imagemodel_form.html', context)