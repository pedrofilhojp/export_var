#https://github.com/prometheus/client_python
import prometheus_client as prom
from prometheus_client import Info, Counter, Enum, Histogram
import random
import time
import os

#req_summary = prom.Summary('python_my_req_example', 'Time spent processing a request')
PORT = 11001


list_vars_app=[
    "CONTA_UNICA_URL",
    "CONTA_UNICA_REDIRECT_URI",
    "NATS_BROKER_HOST",
    "NATS_HOST",
    "NATS_QUEUE_GROUP_PREFIX",
    "CRONOS_API_URL"
]

if __name__ == '__main__':


    print("Iniciando o servico na porta: ",PORT)
    prom.start_http_server(PORT)


    c = Counter('VAR_APP', 'Variaveis importantes da aplicacao', ['var', 'content'])
    for var_app in list_vars_app:
        if os.getenv(var_app):
            c.labels(var_app, os.getenv(var_app)).inc()
    
    
    list_vars_metrics = {}
    for var_app in list_vars_app:
        if os.getenv(var_app):
            if list_vars_metrics.get("VAR_APP_"+var_app) is None:
                list_vars_metrics["VAR_APP_"+var_app] = Info("VAR_APP_"+var_app, 'Variaveis importantes da aplicacao')
                list_vars_metrics["VAR_APP_"+var_app].info({var_app: os.getenv(var_app)})
    while True:
        time.sleep(60)


# export NATS_BROKER_HOST="nats://natsdev.incloud.intelbras.com.br:5555"


