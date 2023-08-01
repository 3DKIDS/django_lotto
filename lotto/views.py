from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
#from django_mldl.site_1.lotto.models import GuessNumbers
from .models import GuessNumbers
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음
    #lottos = GuessNumbers.objects.get(조건) 
    #lottos = GuessNumbers.objects.filter() 
    return render(request, 'lotto/default.html', {'lottos':lottos})

    #return render(request,'lotto/default.html', {})
    #return HttpResponse("<h1 style='color:pink'>Hello, world!</h1>")

def post(request):
    print('\n\n\n')
    print(request.method)
    print(request.POST)
    print('\n\n\n')
    if request.method == "POST":
        form = PostForm(request.POST) # 상단 from .forms import PostForm 추가
        if form.is_valid():
	    # 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류함
            lotto = form.save(commit = False) # 최종 DB 저장은 아래 generate 함수 내부의 .save()로 처리
            print(type(lotto)) # <class 'lotto.models.GuessNumbers'>
            print(lotto)
            lotto.generate()
            return redirect('index') # urls.py의 name='index'에 해당
            # -> 상단 from django.shortcuts import render, redirect 수정

    else:
        form = PostForm() # empty form
        return render(request, "lotto/form.html", {"form": form})

            
    
def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
    return render(request, "lotto/detail.html", {"lotto": lotto})



def hello(request):
    # data = GuessNumbers.objects.all()
    # data = GuessNumbers.objects.get(id=1)
    return HttpResponse("<h1 style='color:black;'>Hello, main!</h1>")





# user_input_name = request.POST['name']
    # user_input_text = request.POST['text']
    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)
    # print(new_row.num_lotto)
    # print(new_row.name)
    # new_row.name = new_row.name.upper()
    
    # new_row.generate()
    
   #new_row.lottos = [np.randint(1, 45) for i in range(6)]
    # new_row.lottos = ""
    # origin = list(range(1,46)) # 1~45의 숫자 리스트 [1, 2, 3, ..., 43, 44, 45]
    #     # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
    # for _ in range(0, new_row.num_lotto):
    #     random.shuffle(origin) # [10, 21, 36, 2, ... , 1, 11]
    #     guess = origin[:6] # [10, 21, 36, 2, 15, 23]
    #     guess.sort() # [2, 10, 15, 21, 23, 36]
    #     new_row.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가 -> '[2, 10, 15, 21, 23, 36]\n'
    #     # self.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
    # new_row.update_date = timezone.now()
    # new_row.save() # GuessNumbers object를 DB에 저장