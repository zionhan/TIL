from bs4 import BeautifulSoup as bs

html = '''
<html>
    <head>    
        <title>BeautifulSoup test</title>
    </head>
    <body>
        <div id='upper' class='test' custom='good'>
            <h3 title='Good Content Title'>Contents Title</h3>
            <p>Test contents</p>
        </div>
        <div id='lower' class='test' custom='nice'>
            <p>Test Test Test 1</p>
            <p>Test Test Test 2</p>
            <p>Test Test Test 3</p>
        </div>    
    </body>
</html>
'''

soup = bs(html)
# find, 첫번째 태그
print( soup.find( 'h3' ) )
print( soup.find( 'p' ) )
print( soup.find( 'div', custom='nice' ) )
print( soup.find( 'div', id='lower' ) )
print( soup.find( 'div', class_='test' ) )

attrs = {'id': 'upper', 'class': 'test'}
print( soup.find( 'div', attrs=attrs ) )


# find_all, 모든 태그를 리스트 형식으로 반환.
print( soup.find_all( 'div', class_='test' ) )

# get_text(), 
tag = soup.find('h3').get_text()
print( tag )

tag = soup.find( 'div' ).get_text()
print( tag )

# attr값 가져올 경우
tag = soup.find('h3')['title']
print( tag )
