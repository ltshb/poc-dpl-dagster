# Setup Dagster on Kubernetes

To setup Dagster on the swissgeo poc-datapipeline Kubernetes cluster, follow the steps below:

1. Login to AWS with your SSO credentials
2. Select the cluster via kubectl
3. Enter

```bash
k diff -k helm-dagster-rendered/base/
```
