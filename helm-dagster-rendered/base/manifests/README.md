# Installation of dagster on kubernetes with helm

Refer to https://docs.dagster.io/deployment/oss/deployment-options/kubernetes/deploying-to-kubernetes

1. Add repo

```bash
helm repo add dagster https://dagster-io.github.io/helm
```

2. Get default values

```bash
helm show values dagster/dagster > default-values.yaml
```

3. Create initial values file

```bash
cp default-values.yaml values.yaml
```

4. Render helm chart

```bash
helm template dagster/dagster -f values.yaml --namespace dagster > rendered.yaml
```
