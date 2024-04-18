from django import forms


class ArticleForm(forms.Form):
    # 앞은 데이터베이스에 저장될 값, 뒤는 사용자에게 보여질 값
    GENRE_CHOICES = [
        ("technology", "Technology"),
        ("life", "Life"),
        ("hobby", "Hobby"),
    ]

    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
