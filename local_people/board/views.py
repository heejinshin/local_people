from django.shortcuts import render
from .models import Board
# Create your views here.
def list(request):
    print("")
    # boardList = Board.objects.all()
    # boardList = Board.objects.order_by('-id')
    # return render(request, "board/board_list.html", {'boardList':boardList} )

def create(request):
    board = Board() 
    board.title = request.GET['title']
    board.writer = request.GET['writer']
    board.contents = request.GET['contents']
    board.save()
    return

#조회 
#queryset = 모델 클래스명.objects.all()
#queryset = queryset.filter(조건필드1 = 조건값1, 조건필드2 = 조건값2)
#queryset = queryset.filter(조건필드3 = 조건값3)
#question_list = Board.objects.order_by('-wdate')
#print(connection)
#mysql -u root -p --port = 5036

import pymysql
conn = pymysql.connect(host = 'localhost', user = 'user01', password =
'1234' ,db = 'mydb', port=5306)
curs = conn.cursor()
sql = "SELECT 1 id, title, writer, date_format(wdate, '%Y-%m-%d') wdate, contents, hit+10 hit FROM board_board"
curs.execute(sql) # 쿼리문 실행

rows = curs.fetchall() # 데이터 패치
for row in rows :
    print(row)
conn.close()