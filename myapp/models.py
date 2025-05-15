from django.db import models
from datetime import date

class Department(models.Model):
    code = models.CharField(max_length=20, unique=True)  # 부서코드
    name = models.CharField(max_length=100)              # 부서명
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')  # 상위부서

    def __str__(self):
        return f"{self.code} - {self.name}"

class Rank(models.Model):  # 직급
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0, help_text="정렬 순서")
    
    class Meta:
        ordering = ['order']  # 기본 정렬을 순번 기준으로
        
    def __str__(self):
        return self.name

class Position(models.Model):  # ex) 과장, 팀장 등
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0, help_text="정렬 순서")
    
    class Meta:
        ordering = ['order']  # 기본 정렬을 순번 기준으로

    def __str__(self):
        return self.name

class PositionTitle(models.Model):  # 직책
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0, help_text="정렬 순서")
    
    class Meta:
        ordering = ['order']  # 기본 정렬을 순번 기준으로
        
    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True, error_messages={
        'unique': '이미 존재하는 사번입니다.',})  # 사번
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)  # 직급
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, blank=True)
    position_title = models.ForeignKey(PositionTitle, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=100)     # 직무
    years_worked = models.IntegerField()        # 년차
    ssn = models.CharField(max_length=20)       # 주민등록번호
    birth_date = models.DateField()
    hire_date = models.DateField(verbose_name="입사일")
    resign_date = models.DateField(verbose_name="퇴사일", null=True, blank=True)
    STATUS_CHOICES = [
        ('재직', '재직'),
        ('퇴직', '퇴직'),
        ('휴직', '휴직'),
    ]
    # 휴직종류 선택지
    LEAVE_TYPE_CHOICES = [
        ('육아휴직', '육아휴직'),
        ('산재휴가', '산재휴가'),
        ('출산휴가', '출산휴가'),
        ('일반휴직', '일반휴직'),
        ('기타', '기타'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='재직',
        verbose_name="상태"
    )
    leave_type = models.CharField(
        max_length=50,            # (100까지 필요 없음, 50이면 충분)
        choices=LEAVE_TYPE_CHOICES,
        blank=True,
        verbose_name="휴직종류"
    )
    leave_start_date = models.DateField(null=True, blank=True, verbose_name="휴직 시작일")
    leave_end_date = models.DateField(null=True, blank=True, verbose_name="휴직 종료일")
    
    position_start_date = models.DateField(null=True, blank=True, verbose_name="직급 기준일")
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('정규직', '정규직'),
        ('계약직', '계약직'),
        ('아르바이트', '아르바이트'),
    ]
    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default='정규직',
        verbose_name="고용형태"
    )
    
    address = models.CharField(max_length=255, blank=True, verbose_name="주소")
    photo = models.FileField(
        upload_to='employee_photos/',
        blank=True,
        null=True,
        verbose_name="사진",
        help_text="jpg, jpeg, png만 업로드 가능합니다.",)
    email = models.EmailField(max_length=100, blank=True, verbose_name="이메일")
    phone = models.CharField(max_length=20, blank=True, verbose_name="연락처")
    gender = models.CharField(max_length=10, blank=True, verbose_name="성별")  # "남" 또는 "여"
    age = models.PositiveIntegerField(null=True, blank=True)  # ✅ 일반 필드로 정의
       
    def save(self, *args, **kwargs):
        # 주민등록번호 기반 생년월일 및 성별 자동 계산
        if self.ssn and len(self.ssn) >= 7:
            yy = int(self.ssn[0:2])
            mm = int(self.ssn[2:4])
            dd = int(self.ssn[4:6])
            gender_code = self.ssn[6]

            if gender_code in ['1', '2']:
                year = 1900 + yy
            elif gender_code in ['3', '4']:
                year = 2000 + yy
            else:
                year = 1900 + yy  # 예외적 상황에 대비한 기본값

            try:
                birth = date(year, mm, dd)
                self.birth_date = birth

                # ✅ 나이 계산 정확
                self.age = date.today().year - birth.year - (
                    (date.today().month, date.today().day) < (birth.month, birth.day)
                )

                # ✅ 성별 설정
                if gender_code in ['1', '3']:
                    self.gender = "남"
                elif gender_code in ['2', '4']:
                    self.gender = "여"
            except Exception:
                pass  # 날짜 형식 오류 등 예외 발생 시 무시
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} ({self.employee_id})"
    
class Career(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="careers")
    company = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=200, blank=True)
    
class Education(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="educations")
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Certification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="certifications")
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True)
    acquired_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)

class SalaryInfo(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="salary_info")
    annual_salary = models.IntegerField(blank=True, null=True)
    monthly_salary = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    account_holder = models.CharField(max_length=50, blank=True, null=True)
    bank_code = models.CharField(max_length=10, blank=True, null=True)
    
    # ✅ 급여 상세 항목 추가
    base_salary = models.IntegerField(blank=True, null=True)
    fixed_overtime_pay = models.IntegerField(blank=True, null=True)
    meal_allowance = models.IntegerField(blank=True, null=True)
    duty_allowance = models.IntegerField(blank=True, null=True)
    commute_allowance = models.IntegerField(blank=True, null=True)
    childcare_allowance = models.IntegerField(blank=True, null=True)