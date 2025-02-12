Фильтр: https://github.com/orgs/JJOInvest/packages?ecosystem=container

|Image|Trivy|Grype|
|---|---|---|
|docker pull ghcr.io/jjoinvest/jjo-assistant:main|debian: 95; python-pkg: 2|python: 2; deb: 90; binary 1|
|docker pull ghcr.io/jjoinvest/telegram-zendesk-bot:main|debian: 95; python: 8|deb: 90; python: 8; binary 1|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/victoria-metrics-k8s-stack:0.24.5|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/flagsmith:0.53.0|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/ingress-nginx:4.11.1|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/reflector:7.1.288|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/rabbitmq-cluster-operator:4.3.17|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/aws-load-balancer-controller:1.8.1|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/cert-manager:v1.15.2|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/metrics-server:3.12.1|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/vault-operator:1.22.2|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/node-local-dns:2.0.14|-|-|
|docker pull ghcr.io/jjoinvest/dashboard-monoapp:release-0.1.0|debian: 75; node-pkg: 8; gobinary: 49|deb: 70; npm: 7; binary: 2; go-module: 55|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/gateway-helm:v1.1.0|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/kubelinks:0.4.6|-|-|
|docker pull ghcr.io/jjoinvest/miniapp-monoapp:release-0.1.0|debian:75; node-pkg: 8; gobinary: 54|deb: 70; npm: 7; binary: 2; go-module: 55|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/allure-server:1.0.0|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/vault-secrets-webhook:1.21.2|-|-|
|docker pull ghcr.io/jjoinvest/telegram-payment-service:release-1.29.0|debian: 2797; secrets: 3|total: 676|
|docker pull ghcr.io/jjoinvest/jjo-invest-backend-v2/php-actions_composer_jjo-invest-backend-v2:php-latest-build2.1.0|alpine: 184|total: 212|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/allure-testops:4.14.9|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/dex_akka-cluster:1.0.0|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/dex-akka-cluster:1.0.0|-|-|
|docker pull ghcr.io/jjoinvest/lava-services:helm-deploy|debian: 2797; secrets: 3|total: 678|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/rabbitmq:14.4.3|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/redis:19.5.4|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/opensearch:2.26.1|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/mariadb:18.2.3|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/victoria-metrics-agent:0.15.4|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/prometheus-rds-exporter-chart:0.10.1|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/actions-runner-controller:0.23.7|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/prometheus-redis-exporter:6.5.0|-|-|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/jjo:1.0.1|-|-|
|docker pull ghcr.io/jjoinvest/dashboard:release-2.2|alpine: 14; node-pkg: 30; secrets: 6|npm: 29; apk: 16; binary: 6|
|docker pull ghcr.io/jjoinvest/coop-landing-v2:release-1.3.2|-|-|
|docker pull ghcr.io/jjoinvest/mini-app:release-2.2|alpine: 14; node-pkg: 26|npm: 25; apk: 16; binary: 6|
|docker pull ghcr.io/jjoinvest/geosharding-proxy-java:main-testing-mariadb|oracle: 153; jar: 28|total: 179|
|docker pull ghcr.io/jjoinvest/jjo-helm-charts/graylog:2.3.8|-|-|
|docker pull ghcr.io/jjoinvest/maintenance-screen:master|alpine: 14; gobinary: 14|apk: 16; npm: 6; binary: 6; go-module: 14|
|docker pull ghcr.io/jjoinvest/dashboard-newapp:release-0.1.0|debian: 75; gobinary: 54|deb: 70; npm: 9; binary: 2; go-module: 55|

Если в столбце стоит `-`, то значит, что образ не удалось получить из-за ошибки:

```
7.1.288: Pulling from jjoinvest/jjo-helm-charts/reflector
unsupported media type application/vnd.cncf.helm.config.v1+json
```

За исключением образа `ghcr.io/jjoinvest/coop-landing-v2:release-1.3.2`. В данном случае ошибка была во время `pull`:

```
unexpected EOF
```