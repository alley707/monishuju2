# _*_ coding:utf-8 _*_

from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
        self.client.get("http://www.baidu.com")

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8089"
    task = UserBehavior.baidu
    wait_time = between(5, 30)

