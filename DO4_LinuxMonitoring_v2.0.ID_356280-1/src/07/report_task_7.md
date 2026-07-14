## 1. Установка программ.

 - sudo apt install prometheus-node-exporter
 - systemctl status prometheus-node-exporter

 ![stastus_node](../../misc/screenshots/07_status_node.png)

 - sudo apt install prometheus
 - systemctl status prometheus

 ![status_prometheus](../../misc/screenshots/07_status_prometheus.png)

 - curl http://localhost:9090/api/v1/targets

 ![prom_check_node](../../misc/screenshots/07-prometheus_check_node.png)

  > - localhost:9100 - есть
  > - health: up - есть
  > 
  > **Итог:** Prometheus видит Node Exporter

 - wget https://dl.grafana.com/oss/release/grafana_10.4.2_amd64.deb
 - sudo dpkg -i grafana_10.4.2_amd64.deb
 - sudo systemctl enable grafana-server
 - sudo systemctl start grafana-server
 - systemctl status grafana-server

 ![status_grafana](../../misc/screenshots/07_status_grafana.png)

## 2. Запуск Grafana в браузере и тесты.

 - http://192.168.0.201:3000
 
 - Добавил Dashboard и добавил в него панели CPU, RAM, Free Disk space, Disk I/0.

 ![grafana_web](../../misc/screenshots/07_grafana_web.png)

 - Запустил скрипт из Part 2.

 ![grafana_web2](../../misc/screenshots/07_grafana_web2.png)

 > **Результат:** После запуска скрипта поднялась загруженность CPU, DISK I/O, уменьшились показатели свободного места в RAM и Disk space.

 - Установил утилиту stress на машину командой 
     ```bash
     sudo apt install stress
     ```
 
 - Запустил утилиту командой 
     ```bash
     stress -c 2 -i 1 -m 1 --vm-bytes 32M -t 10s
     ```
 
 ![grafana_web3](../../misc/screenshots/07_grafana_web3.png)

 > **Результат:** После запуска утилиты поднялись показатели загружености CPU и Disk I/O

 