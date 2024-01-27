from django.contrib.auth.models import Group, User
from django.contrib import auth
from restapi.models import Course, Student
from rest_framework.decorators import action
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from restapi.serializers import GroupSerializer, UserSerializer, CourseSerializer, StudentSerializer
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import json

import vertexai
from vertexai.preview.language_models import TextGenerationModel
import pandas as pd
import re
import random

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request)
        if serializer.is_valid():
            serializer.save()

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        try:
            User.objects.get(username = request.data.get('UserName'))
            return Response("failed")
        except:
            user = User.objects.create(username = request.data.get('UserName'), email = request.data.get('Email'))
            user.set_password(request.data.get('Password'))
            user.save()
            Student.objects.create(UserName = user, Photo = request.data.get('Photo'), University = request.data.get('Department'), Age = request.data.get('Age'))
            return Response("ok")
    
    def update(self, request):
        user = User.objects.filter.update(username = request.data.get('UserName'), email = request.data.get('Email'), password = request.data.get('Password'))
        Student.objects.update(UserName = user, Photo = request.data.get('Photo'), University = request.data.get('Department'), Age = request.data.get('Age'))
        return Response("ok")
    
    @action(methods = ['get'], detail = False) 
    def printUser(self, request):
        print(request.user)
        return Response(Student.objects.get(UserName = User.objects.get(username = request.user)).Photo)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    


    ### 學習路徑 推薦課程(用在搜尋框)
    @action(methods=['get'], detail=False)
    def recommend_course(self,_):
        def predict_large_language_model(
            model_name: str,
            temperature: float,
            max_output_tokens: int,
            top_p: float,
            top_k: int,
            content: str,
            tuned_model_name: str = "",
            ) :
            
            model = TextGenerationModel.from_pretrained(model_name)
            if tuned_model_name:
                model = model.get_tuned_model(tuned_model_name)
            response = model.predict(
                content,
                temperature=temperature,
                max_output_tokens=max_output_tokens,
                top_k=top_k,
                top_p=top_p,)
            return response.text


        #先從DB讀全部，再sample 70個 (不能一次讀太多筆 input會爆,試試看random sampling)
        data_list = []
        for item in self.queryset:
            row = {
                "Course Name": item.CourceName,
                "University": item.University,
                "Difficulty Level": item.DifficultyLevel,
                "Course Rating": item.CourseRating
            }
            data_list.append(row)
        data = pd.DataFrame(data_list)
        # return Response(data) 
        # return Response(data.to_markdown(index=False))
        
        sampled_courses = data.sample(n=70,random_state=45)
        
        # return Response(sampled_courses.to_dict(orient="records"))
        sampled_data_json = sampled_courses.to_json(orient='records')
        # return Response(sampled_data_json)
        # data_markdown = data.to_markdown(index=False)

        preference = input("請問您對於哪些類型的課程感興趣(只需列領域名稱):")
        task = "Please recommend user 7 courses in our course data according to user's course preference. Reply 'Course name','DifficultyLevel',and 'CourseRating' of recommend courses"

        prompt = f'''
        input: This table contains information about courses. The first row includes the table headers, while each subsequent row displays the corresponding data separated by the "|" symbol.
        {sampled_data_json}

        User's preference: {preference}


        Task: {task}
        '''

        response_text = predict_large_language_model(
            "text-bison@001", 
            temperature=0.2, 
            max_output_tokens=256, 
            top_p=0.8, 
            top_k=1, 
            content=prompt)
        # print(response_text)
        return Response(response_text)




    ### 學習課程-排序
    # 依照困難程度排序(low to high)
    @action(methods=['get'], detail=False)
    def sort_by_difficulty_asc(self,_):
        difficulty_order = ["Conversant", "Beginner", "Intermediate", "Advanced", "Not Calibrated"]
        # Sort by difficulty level
        sorted_queryset = sorted(self.queryset, key=lambda x: difficulty_order.index(x.DifficultyLevel))
        sorted_queryset_top10 = sorted_queryset[:10]    # 取top 10
        # Serialize 
        serializer = CourseSerializer(sorted_queryset_top10, many=True)

        return Response(serializer.data)
    
    # 依照困難程度排序(high to low)
    @action(methods=['get'], detail=False)
    def sort_by_difficulty_desc(self,_):
        difficulty_order = ["Advanced","Intermediate","Beginner","Conversant", "Not Calibrated" ]
        # Sort by difficulty level
        sorted_queryset = sorted(self.queryset, key=lambda x: difficulty_order.index(x.DifficultyLevel))
        sorted_queryset_top10 = sorted_queryset[:10]    # 取top 10
        # Serialize 
        serializer = CourseSerializer(sorted_queryset_top10, many=True)

        return Response(serializer.data)
    
    # 依照評價排序(low to high)
    @action(methods=['get'], detail=False)
    def sort_by_rating_asc(self,_):
        # 排除NaN值 以及 從最小0.1開始輸出
        sorted_courses = self.queryset.exclude(CourseRating=-1).filter(CourseRating__gte=0.1).order_by('CourseRating')[:10]
        # Serialize
        serializer = CourseSerializer(sorted_courses, many=True)

        return Response(serializer.data)


    # 依照評價排序(high to low)
    @action(methods=['get'], detail=False)
    def sort_by_rating_desc(self,_):
        # Sorting by CourseRating in descending order
        sorted_courses = self.queryset.order_by('-CourseRating')[:10]  
        # Serialize
        serializer = CourseSerializer(sorted_courses, many=True)

        return Response(serializer.data)
    
    # 依照大學名稱排序(A to Z)
    @action(methods=['get'], detail=False)
    def sort_by_university_name_A(self,_):
        # Sorting by University (A to Z) (排除特殊字元開頭)
        sorted_courses = self.queryset.filter(University__regex=r'^[A-Za-z]').order_by('University')[:10]  
        # Serialize
        serializer = CourseSerializer(sorted_courses, many=True)

        return Response(serializer.data)
    
    # 依照大學名稱排序(Z to A)
    @action(methods=['get'], detail=False)
    def sort_by_university_name_Z(self,_):
        # Sorting by University (Z to A) (排除特殊字元開頭)
        sorted_courses = self.queryset.filter(University__regex=r'^[A-Za-z]').order_by('-University')[:10]
        # Serialize
        serializer = CourseSerializer(sorted_courses, many=True)

        return Response(serializer.data)
    
   
    ### 學習歷史紀錄(show)
    @action(methods=['get'], detail=False)
    def show_user_learing_record(self,_):
        pass


    ### 學習歷程(上次學習的是哪堂課)(history list中的最後一筆)
    @action(methods=['get'], detail=False)
    def show_user_last_learning_record(self,_):
        pass
    


    ### 學習成果/獎勵  (更新和show) -> 給前端用
    # @action(methods=['get'], detail=False)
    # def update_user_exp(self,_):
    #     pass

    # @action(methods=['get'], detail=False)
    # def show_user_exp(self,_):
    #     pass



    ### 類似背景的人也在學習什麼?(你可能感興趣的課程)
    @action(methods=['get'], detail=False)
    def recommend_courses_by_related_deparment(self,_):
        def predict_large_language_model(
            model_name: str,
            temperature: float,
            max_output_tokens: int,
            top_p: float,
            top_k: int,
            content: str,
            tuned_model_name: str = "",
            ) :
            
            model = TextGenerationModel.from_pretrained(model_name)
            if tuned_model_name:
                model = model.get_tuned_model(tuned_model_name)
            response = model.predict(
                content,
                temperature=temperature,
                max_output_tokens=max_output_tokens,
                top_k=top_k,
                top_p=top_p,)
            return response.text


        #先從DB讀全部，再sample 70個 (不能一次讀太多筆 input會爆,試試看random sampling)
        data_list = []
        for item in self.queryset:
            row = {
                "Course Name": item.CourceName,
                "University": item.University,
                "Difficulty Level": item.DifficultyLevel,
                "Course Rating": item.CourseRating
            }
            data_list.append(row)
        data = pd.DataFrame(data_list)
        # return Response(data) 
        # return Response(data.to_markdown(index=False))
        
        sampled_courses = data.sample(n=70,random_state=35)
        
        # return Response(sampled_courses.to_dict(orient="records"))
        sampled_data_json = sampled_courses.to_json(orient='records')
        # return Response(sampled_data_json)
    

        #TODO 改成從user的科系去讀(不寫死)
        department = "Economic"
        task = "Please recommend user 5 courses in our course data related to user's department. Reply 'Course name','DifficultyLevel',and 'CourseRating' of recommend courses"

        prompt = f'''
        input: This table contains information about courses. The first row includes the table headers, while each subsequent row displays the corresponding data separated by the "|" symbol.
        {sampled_data_json}

        User's deparment: {department}

        Task: {task}
        '''

        response_text = predict_large_language_model(
            "text-bison@001", 
            temperature=0.2, 
            max_output_tokens=256, 
            top_p=0.8, 
            top_k=1, 
            content=prompt)
        # print(response_text)
        return Response(response_text)

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return HttpResponse('ok')
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        print(request.user)
        return HttpResponse('ok')
    else:
        return HttpResponse('failed')
    