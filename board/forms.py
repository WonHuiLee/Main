from django import forms
from board.models import Question, Answer, Question2


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        textarea = {
            'subject': '',
            'content': '',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        textarea = {
            'content': '',
        }


class Question2Form(forms.ModelForm):
    class Meta:
        model = Question2  # 사용할 모델
        fields = ['subject', 'content']  # Question2Form에서 사용할 Question2 모델의 속성
        textarea = {
            'subject': '',
            'content': '',
        }