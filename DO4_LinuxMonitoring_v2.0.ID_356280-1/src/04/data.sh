#!/bin/bash

status_codes=(200 201 301 302 400 401 403 404 500 501 502 503)
methods=("GET" "POST" "PUT" "PATCH" "DELETE")
urls=("/index.html" "/contacts" "/register" "/login" "/dashboard" "/profile" "/settings" "/search" "/products")
agents=("Mozilla/5.0" "Chrome/90.0" "Safari/14.0" "Edge/91.0" "Opera/76.0")

# 200 OK - запрос успешно обработан
# 201 Created - ресурс успешно создан
# 301 Moved Permanently - ресурс навсегда перенесён на другой URL
# 302 Found - ресурс временно доступен по другому URL
# 400 Bad Request - сервер не смог понять запрос из-за неверного формата
# 401 Unauthorized - требуется авторизация
# 403 Forbidden - доступ к ресурсу запрещён
# 404 Not Found - запрошенный ресурс не найден
# 500 Internal Server Error - внутренняя ошибка сервера
# 501 Not Implemented - сервер не поддерживает запрошенный метод или функциональность
# 502 Bad Gateway - сервер получил некорректный ответ от вышестоящего сервера
# 503 Service Unavailable - сервер временно недоступен или перегружен

