import reflex as rx
import redis
import datetime as date

# Create a Redis connection pool
redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

class RedisState(rx.State):
    key: str = ""
    result: str = ""

    _date: date = date.datetime.now().strftime("%Y-%m-%d")
    dataArr: list[str] = ["0My day was good", "0I faced issue while developing", "0Happy", "0summary4321"]# q1, q2, mood, summary
    task: str = ""
    q1: str = ""
    q2: str = ""
    mood: str = ""
    summary: str = ""

    @property
    def redis_client(self):
        return redis.Redis(connection_pool=redis_pool)

    def set_key(self, key: str):
        self.key = key

    def set_task(self, value: str):
        print("setval:", value)
        self.task = value

    def insert_data(self):
        try:
            self.redis_client.set(self.key, self.task)
            self.result = f"Successfully inserted: {self.key} = {self.task}"
        except Exception as e:
            self.result = f"Error inserting data: {str(e)}"

    def insert_task(self): #tbd
        print("insert:", self.task)
        try:
            self.redis_client.set(self._date, self.task) 
        except Exception as e:
            self.result = f"Error inserting data: {str(e)}"

    def insert_all(self):
        self.q1 = "My day was good"
        self.q2 = "I faced issue while developing"
        self.mood = "Happy"
        self.summary = "summary4321"
        self.dataArr = [self.q1, self.q2, self.mood, self.summary]
        # self.dataArr.append([self.q1, self.q2, self.mood, self.summary])
        print("insert:", self._date, self.dataArr)
        try:
            self.redis_client.set(self._date, self.dataArr)
        except Exception as e:
            self.result = f"Error inserting data: {str(e)}"

    def read_data(self):
        try:
            value = self.redis_client.get(self.key)
            if value:
                self.result = f"Value for {self.key}: {value.decode('utf-8')}"
            else:
                self.result = f"No value found for key: {self.key}"
        except Exception as e:
            self.result = f"Error reading data: {str(e)}"

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
