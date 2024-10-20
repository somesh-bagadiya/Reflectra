import reflex as rx
import redis
import datetime as date
import json 
# Create a Redis connection pool
redis_pool = redis.ConnectionPool(host="localhost", port=6379, db=0)

class RedisState(rx.State):
    key: str = ""
    result: str = ""

    _date: str = f"{date.datetime.now().year}-{date.datetime.now().month}-{date.datetime.now().day}"
    dataArr: list[str] = [] # q1, q2, mood, summary
    task: str = ""
    tasks: list[str] = []
    q1: str = ""
    q2: str = ""
    mood: str = ""
    summary: str = ""

    @property
    def redis_client(self):
        return redis.Redis(connection_pool=redis_pool)

    def set_key(self, key: str):
        self.key = key

    def set_task(self, value: list):
        self.task = (value)

    def set_date(self, value: str):
        self._date = value

    def set_q1(self, value: str):
        print("inside sQ1")
        self.q1 = value

    def set_q2(self, value: str):
        print("inside sQ2")
        self.q2 = value

    def set_summary(self, value: str):
        self.summary = value

    def insert_data(self):
        try:
            self.redis_client.set(self.key, self.task)
            self.result = f"Successfully inserted: {self.key} = {self.task}"
        except Exception as e:
            self.result = f"Error inserting data: {str(e)}"

    def insert_task(self):  # tbd
        print("insert:", self.task)
        try:
            self.redis_client.set(self._date, self.task)
        except Exception as e:
            self.result = f"Error inserting data: {str(e)}"

    async def insert_all(self, localDate:str):
        self.tasks.append(self.task)
        self.task = ""
        # print("type value", type(json.dump(self.tasks)), json.dump(self.tasks))
        self.dataArr = [self.q1, self.q2, self.mood, self.summary]
        print("insert:", localDate, self.dataArr)
        try:
            self.redis_client.rpush(localDate, self.q1, self.q2, self.mood, self.summary)
        except Exception as e:
            self.result = f"Error inserting data: {str(e)}"

    async def read_all(self, date):
        # print("inside read all", date)
        self.tasks = []
        try:
            value = self.redis_client.lrange(date, 0, -1)
            if value:
                self.q1 = value[0].decode('utf-8')
                self.q2 = value[1].decode('utf-8')
                self.mood = value[2].decode('utf-8')
                self.summary = value[3].decode('utf-8')
                # print("type, val:", type(len(json.loads(value[4].decode('utf-8')))), len(json.loads(value[4].decode('utf-8'))))
                if len(json.loads(value[4].decode('utf-8'))) > 0:
                    self.tasks = json.loads(value[4].decode('utf-8'))
            else:
                print("not found", date)
                self.q1 = ""
                self.q2 = ""
                self.mood = ""
                self.summary = ""
                self.tasks = []
        except Exception as e:
            self.result = f"Error reading data: {str(e)}"

    def read_data(self):
        try:
            value = self.redis_client.get(self.key)
            if value:
                self.result = f"Value for {self.key}: {value.decode('utf-8')}"
            else:
                self.result = f"No value found for key: {self.key}"
        except Exception as e:
            self.result = f"Error reading data: {str(e)}"
    
    async def delete_data(self, date):
        print("inside del", date)
        self.redis_client.delete(date)

def index():
    return rx.vstack(
        rx.heading("Redis CRUD Example"),
        rx.input(
            placeholder="Enter key",
            on_change=RedisState.set_key,
            value=RedisState.key,
        ),
        rx.input(
            placeholder="Enter value",
            on_change=RedisState.set_task,
            value=RedisState.task,
        ),
        rx.hstack(
            rx.button("Insert", on_click=RedisState.insert_data),
            rx.button("Read", on_click=RedisState.read_data),
        ),
        rx.text(RedisState.result),
        spacing="4",
        padding="4",
    )
