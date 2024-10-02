from django.shortcuts import render,redirect
from django.views.generic import View
from Myapp.models import Employee,Work
from Myapp.forms import WorkForm

#employeelisting
#url:localhost:8000/employees/all/
# method :get
class EmployeeListView(View):
    def get(self,request,*args, **kwargs):
        
        # orm query for fetching of employee records
        qs=Employee.objects.all()
        return render(request,"employee_list.html",{"employees":qs})
    
#employeeadding
#url:localhost:8000/employee/add
#method:get,post
class EmployeeCreateView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"employee_create.html")
        
    def post(self,request,*args, **kwargs):
        name_box=request.POST.get("nameBox")
        age_box=request.POST.get("ageBox")
        salary_box=request.POST.get("salaryBox")
        designation_box=request.POST.get("designationBox")
        email_box=request.POST.get("emailBox")
        phone_box=request.POST.get("phoneBox")
        place_box=request.POST.get("placeBox")
        Employee.objects.create(name=name_box,age=age_box,salary=salary_box,designation=designation_box,email=email_box,phone=phone_box,place=place_box)
        return redirect("emp-list")


class EmployeeDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,"employee_info.html",{"employee":qs})

class EmployeeDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()
        return redirect ("emp-list")
    
class EmployeeUpdateView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        emp_obj=Employee.objects.get(id=id)
        return render(request,"employee_edit.html",{"employee":emp_obj})
    
    def post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Employee.objects.filter(id=id).update(name=request.POST.get("name"),
        age=int(request.POST.get("age")),
        salary=int(request.POST.get("salary")),
        designation=request.POST.get("designation"),
        email=request.POST.get("email"),
        phone=int(request.POST.get("phone")),
        place=request.POST.get("place"))
        return redirect("emp-list")
    
    
class WorkCreateView(View):
    def get(self,request,*args, **kwargs):
        
        form_instance=WorkForm
        return render(request,"work_add.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        form_instance=WorkForm(request.POST)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            Work.objects.create(**data)
            
            return redirect("work-list")
            
        return render(request,"work_add.html")
    
    
class WorkListView(View):
    def get(self,request,*args, **kwargs):
        qs=Work.objects.all()
        return render(request,"work_list.html",{"works":qs})
    
class WorkUpdateView(View):
    
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        work_object=Work.objects.get(id=id)
        data={
            "title":work_object.title,
            "description":work_object.description,
            "start_date":work_object.start_date,
            "end_date":work_object.end_date,
            "status":work_object.status
        }
        form_instance=WorkForm(initial=data)
        return render(request,"work.update.html",{"form":form_instance})
    
    def post(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        form_instance=WorkForm(request.POST)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            Work.objects.filter(id=id).update(**data)
            
            return redirect("work-list")
        
        return render(request,"work.update.html",{"form":form_instance})
    

class WorkDeleteView(View):
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        
        Work.objects.get(id=id).delete()
        
        return redirect("work-list")