from django import forms
from .models import Employee, Department, Rank, PositionTitle, Position

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['code', 'name', 'parent']
        labels = {
            'code': '부서코드',
            'name': '부서명',
            'parent': '상위부서',
        }

class EmployeeForm(forms.ModelForm):
    # 생년월일 입력을 달력으로
  
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='생년월일'      # 한글 레이블 추가
    )
    hire_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='입사일'        # 한글 레이블 추가
    )
    resign_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label='퇴사일'        # 한글 레이블 추가
    )

    age = forms.IntegerField(label='나이', required=False, disabled=True)

    class Meta:
        model = Employee
        fields = '__all__'
        exclude = []  # 또는 필요한 필드 명시
        labels = {
            'employee_id': '사번',
            'name': '이름',
            'department': '부서',
            'position': '직급',
            'rank': '직위',
            'role': '직무',
            'years_worked': '년차',
            'birth_date': '생년월일',
            'ssn': '주민등록번호',
            'education': '학력',
            'career': '경력',
            'certifications': '자격사항',
            'annual_salary': '연봉',
            'monthly_salary': '월급여',
            'bank_name': '은행명',
            'account_number': '계좌번호',
            'account_holder': '예금주',
            'status': '상태',
            'leave_type': '휴직종류',
            'leave_start_date': '휴직 시작일',
            'leave_end_date': '휴직 종료일',
            'position_start_date': '직급 기준일',
            'employment_type': '고용형태',
            'address': '주소',
            'email': '이메일',
            'photo': '사진',
            'phone': '연락처',
            'gender': '성별',
            'position_title': '직책',
        }
        error_messages = {
            'employee_id': {
                'unique': '이미 존재하는 사번입니다.',
            },
        }
        widgets = {
            'photo': forms.ClearableFileInput(attrs={
                'style': 'display: none;',  # 기본 UI 숨김
                'id': 'id_photo_hidden_input'
            }),
        }

class RankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = ['name', 'order']
        labels = {
            'name': '직급명',
            'order': '순번',
        }


class PositionTitleForm(forms.ModelForm):
    class Meta:
        model = PositionTitle
        fields = ['name', 'order']
        labels = {
            'name': '직급명',
            'order': '순번',
        }
        
class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'order']
        labels = {
            'name': '직급명',
            'order': '순번',
        }