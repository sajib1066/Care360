from django.contrib import admin
from .models import (
    Position, Employee, Attendance, Leave,
    Payroll, Performance, Recruitment
)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department')
    list_filter = ('department',)
    search_fields = ('title',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'position', 'phone', 'joining_date')
    list_filter = ('position', 'gender')
    search_fields = ('employee_id', 'user__username', 'phone')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in', 'check_out', 'status')
    list_filter = ('date', 'status')
    search_fields = ('employee__employee_id',)

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status')
    list_filter = ('leave_type', 'status')
    search_fields = ('employee__employee_id',)

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'period_start', 'period_end', 'net_salary', 'payment_status')
    list_filter = ('payment_status', 'period_start')
    search_fields = ('employee__employee_id',)

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'review_date', 'reviewer', 'rating')
    list_filter = ('rating', 'review_date')
    search_fields = ('employee__employee_id',)

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('candidate_name', 'position', 'application_date', 'status')
    list_filter = ('status', 'position')
    search_fields = ('candidate_name', 'email')