from django import forms

from articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__" # 모든 필드를 다 가져와서 모델로 만들어줘
        # exclude = ["title"] # 대신 그 중에 타이틀만 빼주고 (제외)
