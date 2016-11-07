
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self.login()
        pass

    @task
    def profile(self):
        self.client.get("/nonprofit/ifrc", headers={"host":"www.qammado.com"})

    # @task
    # def profile(self):
    #     self.client.get("/nonprofit/ifrc/articles/125585", headers={"host":"www.qammado.com"})


    # @task
    # def profile(self):
    #     self.client.get("/nonprofit/ifrc/campaigns/1", headers={"host":"www.qammado.com"})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=15000