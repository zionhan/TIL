# 단순한 해결 
### 1. base.css 수정
- *재댓글의 재댓글* 부터는 **padding-left : 0rem** 으로 하여 *댓글의 재댓글* 과 간격을 동일하게 함
```css
.gb-padding-left_x-large > .gb-padding-left_x-large {
  padding-left: 0rem;
}
```
#


# 인스타그램을 참고하여 추가적으로 
### 2. _comment.html 수정 ( 인스타그램을 참고하여 댓글 목록 구현 )
- 재댓글들의 ""comment_id""를 댓글의 ""comment.pk""를 향하게 하여 모든 재댓글은 관련 댓글을 기준으로 정렬되게 하였다.
- 추가로 **Comment** 클래스를 **created_datetime** 값으로 정렬하여 오름차순으로 댓글들이 정렬되게 했다
```html
 {% if comment.comment %}
  <input type="hidden" required="true" name="comment_id" value="{{ comment.comment_id }}"/>
 {% else %}
  <input type="hidden" required="true" name="comment_id" value="{{ comment.pk }}"/>
 {% endif %}
```

```python
class Meta:
  ordering = ['created_datetime']
```

### 3. models.py 수정
- 댓글 삭제시 연관 재댓글들 모두 삭제되게 함
- 재댓글의 삭제는 다른 재댓글의 영향을 주지 않음
```python
comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)
```

### 4. base.js 수정
- 재댓글 입력창을 "답글달기" 버튼을 눌렀을 때 나타나게 함
```javascript
$(document).ready( function() {
  $("button[class=button]").on(
    "click",
    function(event) {
    var button_id = $(this).attr("id");
    var display_check = $("div[id="+button_id+"]").css("display");

    if( display_check === "none" ) {
      $("div[id="+button_id+"]").css("display", "block");
    } else {
      $("div[id="+button_id+"]").css("display", "none");
    }
 });
});
```
