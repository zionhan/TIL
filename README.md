### base.css 수정 
``` css
.gb-padding-left_x-large > .gb-padding-left_x-large {
  padding-left: 0rem;
}
```


### _comment.html 수정
``` html
 {% if comment.comment %}
  <input type="hidden" required="true" name="comment_id" value="{{ comment.comment_id }}"/>
 {% else %}
  <input type="hidden" required="true" name="comment_id" value="{{ comment.pk }}"/>
 {% endif %}
```

### models.py 수정
``` python
comment = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True)
```
