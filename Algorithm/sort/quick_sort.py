# 시간복잡도  평균 O( NlogN ) 최악의 경우 O( N^2 ) 
'''
퀵정렬(Quick sort)
 - 정렬 알고리즘의 꽃
 - 기준점(pivot)을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right)로 모으는 함수를 작성함
 - 각 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
 * 정렬이 돼있을 수록 느려짐 최악의 경우 O(n^2)
'''
import random

def quick_sort( data, start, end ):
    if( start >= end ) :
        return
    
    low = start + 1
    high = end
    temp = 0
    
    while( low <= high ) : 
        while( low < end and data[low] <= data[start] ) :
            low += 1
            
        while( high > start and data[high] >= data[start]  ) :
            high -= 1
            
        if( low < high ) :
            temp = data[high]
            data[high] = data[low]
            data[low] = temp
        else :
            temp = data[high]
            data[high] = data[start]
            data[start] = temp
    
    quick_sort( data, start, high-1 )
    quick_sort( data, low, end )    
    return


def qsort( data ):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]
#     for index in range( 1, len(data) ):
#         if pivot > data[index]:
#             left.append(data[index])
#         else :
#             right.append(data[index])
    left = [item for item in data[1:] if pivot > item ]
    right = [item for item in data[1:] if pivot <= item ]            
    return qsort(left) + [pivot] +qsort(right)


data = random.sample( range(100), 10 )     
quick_sort( data, 0, len( data )-1 )
print( data )

print( qsort(data) )


