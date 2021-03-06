# for 문의 시간 복잡도 O(N)
# sort 하는 시간을 줄이기 위해 heapq 모듈 사용 정렬 시간 복잡도 ( O(logN) )
# 총 시간 복잡도 O(NlogN)
# 인터넷에서 복사한거 바로 처리 
import heapq as hq

text = """낮음, 1, A.로그인 화면 오타 수정

긴급, 3, B.OTP 사용자 로그인 안됨

보통, 1, C.권한 안내 문구 수정

낮음, 2, D.로딩중 표시 아이콘 변경

긴급, 3, E.메일의 본문이 표시되지 않는 문제

보통, 1, F.첨부파일 사이즈 표시 오류 수정

긴급, 2, G.메일 전송시 첨부파일 누락됨

보통, 3, H.1:1 문의 기능 구현

낮음, 1, I.제품 로고 변경

보통, 3, J.안읽음 카운트 오류 문제 

낮음, 1, K.폰트 색상 변경 

긴급, 2, L.전체 메일함 동기화 안되는 문제 """

bug_list = []
first_bug_list = []     # "긴급" 버그 리스트
second_bug_list = []    # "보통" 버그 리스트
third_bug_list = []     # "낮음" 버그 리스트

def viewList( bug_list ) :
    while( bug_list ) :
        bug = hq.heappop( bug_list )[1]
        print( "{},{},{}".format( bug[0], bug[1], bug[2] ) )
    print() 
  
for line in text.split( "\n" ) :
    if( line != "" ) :        
        bug_list.append( line.split(",") )
   
for bug in bug_list :    
    priority = bug[0]    
    sortBy = str( bug[1] ) + bug[2][0]            
    if( priority == "긴급" ) :
        hq.heappush( first_bug_list, (sortBy, bug) )
    elif( priority == "보통" ) :
        hq.heappush( second_bug_list, (sortBy, bug) )
    elif( priority == "낮음" ) :
        hq.heappush( third_bug_list, (sortBy, bug) )   

viewList( first_bug_list )
viewList( second_bug_list )
viewList( third_bug_list )

        