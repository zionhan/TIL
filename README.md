### 1. base.css 수정 
- 단순한 해결 : 재댓글의 재댓글 부터는 **padding-left : 0rem** 으로 하여 간격을 동일하게 함
```css
.gb-padding-left_x-large > .gb-padding-left_x-large {
  padding-left: 0rem;
}
```


### 2. _comment.html 수정
```html
 {% if comment.comment %}
  <input type="hidden" required="true" name="comment_id" value="{{ comment.comment_id }}"/>
 {% else %}
  <input type="hidden" required="true" name="comment_id" value="{{ comment.pk }}"/>
 {% endif %}
```

### 3. models.py 수정
- 댓글 삭제시 연관 재댓글들 모두 삭제되게 함( 인스타그램 참고 )
```python
comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)
```

### 4. base.js 수정
- 재댓글 입력창을 "답글달기" 버튼을 눌렀을 때 나타나게 함( 인스타그램 참고 )
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
