FROM nginx:1.27

RUN apt-get update && \
    apt-get install -y gcc make libfcgi-dev spawn-fcgi && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY server/server.c .

RUN gcc -o server server.c -lfcgi && \
    chown -R nginx:nginx /app

RUN rm -f /etc/nginx/conf.d/default.conf

COPY nginx/nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /var/cache/nginx /var/run/nginx /run/nginx /var/log/nginx && \
    chown -R nginx:nginx /var/cache/nginx /var/run/nginx /run/nginx /var/log/nginx

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost/ || exit 1


RUN echo '#!/bin/bash\n\
spawn-fcgi -p 8080 -n /app/server &\n\
nginx -g "daemon off;"' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

USER nginx

EXPOSE 80 8080

ENTRYPOINT ["/entrypoint.sh"]
