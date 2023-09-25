from rest_framework import serializers
from .models import Goal, Task, If_then, User
from django.contrib.auth import authenticate

class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = '__all__'

    def validate(self, data):
        if self.context.get('request.user.id') != data.get('user'):
            raise serializers.ValidationError('他ユーザーデータへのアクセスは許されていません。')
        return data

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id', 'content', 'goal', 'if_then_id', 'if_then_content', ]
    
    if_then_content = serializers.ReadOnlyField(source='if_then.content')
    if_then_id = serializers.ReadOnlyField(source='if_then.id')
    
    def validate(self, data):
        goal_id = data['goal'].id
        user_id = Goal.objects.get(id=goal_id).user_id
        if self.context.get('request.user.id') != user_id:
            raise serializers.ValidationError('他ユーザーデータへのアクセスは許されていません。')
        return data

class TaskListSerializer(serializers.ListSerializer):
    child = TaskSerializer()

class GoalTaskSerializer(serializers.ModelSerializer):
    task_set = TaskListSerializer()

    class Meta:
        model = Goal
        fields = ['user','id', 'content', 'status', 'task_set', ]

class GoalTaskListSerializer(serializers.ListSerializer):
    child = GoalTaskSerializer()

class If_thenSerializer(serializers.ModelSerializer):

    class Meta:
        model = If_then
        fields = '__all__'

    def validate(self, data):
        task = data['task']
        user_id = Goal.objects.get(id=task.goal.id).user_id
        if self.context.get('request.user.id') != user_id:
            raise serializers.ValidationError('他ユーザーデータへのアクセスは許されていません。')
        return data