from collections import Counter, defaultdict, deque
from functools import lru_cache, partial
from itertools import chain

requests = [
    "GET",
    "POST",
    "GET",
    "GET",
    "DELETE",
    "POST",
    "GET",
]

counter = Counter(requests)

print(counter["GET"])
print(counter["POST"])
print(counter.most_common(2))

# 2
users = [
    ("Armen", "backend"),
    ("Alex", "frontend"),
    ("John", "backend"),
    ("Kate", "frontend"),
    ("Mike", "devops"),
]

def_dict = defaultdict(list)
for user in users:
    def_dict[user[1]].append(user[0])

print(def_dict)

# 3

deq = deque()

deq.append("A")
deq.append("B")
deq.append("C")

deq.append("D")
deq.appendleft("X")
deq.popleft()
deq.pop()

print(deq)


# 4

@lru_cache(maxsize=10)
def calculate(number):
    print("calculate")
    return number ** 2


print(calculate(5))
print(calculate(5))
print(calculate(10))
print(calculate(5))


# два раза напечатается calculate

# 5
def build_url(host, path, https):
    https = "https" if https else "http"
    return f"{https}://{host}{path}"


build_api_url = partial(build_url, host="api.example.com", https=True)

print(build_api_url(path="/users"))

# 6
backend = ["Django", "FastAPI"]
database = ["PostgreSQL", "Redis"]
print(list(chain(backend, database)))

# 7
logs = [
    ("INFO", "server started"),
    ("ERROR", "database failed"),
    ("INFO", "request received"),
    ("ERROR", "timeout"),
    ("WARNING", "slow request"),
    ("INFO", "response sent"),
]

counter = Counter(logs)

def_dict = defaultdict(list)
for log in logs:
    def_dict[log[0]].append(log[1])

print(counter)
print(def_dict)
