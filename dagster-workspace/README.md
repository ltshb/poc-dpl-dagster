# Dagster

## 1. Dagster Workspace

Scaffolding using

```bash
uvx create-dagster workspace dagster-workspace
cd dagster-workspace
```

## 2. Dagster Projects

Scaffolding projects using

```bash
uvx create-dagster project projects/pipeline-1
uvx create-dagster project projects/pipeline-2
```

## 3. Scaffolding Dagster Docker

```bash
cd dagster-workspace/deployments/local
uv run zsh
# Go back to the workspace directory
cd ../..
dg scaffold build-artifacts
```

## 4. Adding dagster-postgres to each pipeline

`dagster-postgres` is needed in both projects

```bash
cd projects/pipeline-1
uv add dagster-postgres
cd ../pipeline-2
uv add dagster-postgres
```

## 5. Remove the dagster-cloud check in Dockerfile

The generated Dockerfile include a check for `dagster-cloud`, which is not needed for
OSS deployment, it is only needed for dagster+ cloud deployment.

So in both project dockerfile remove the `dagster-cloud` check.

```diff
--- a/dagster-workspace/projects/pipeline-1/Dockerfile
+++ b/dagster-workspace/projects/pipeline-1/Dockerfile
@@ -32,9 +32,3 @@ COPY --from=builder /app /app
 ENV PATH="/app/.venv/bin:$PATH"

 WORKDIR /app
-
-# Make sure dagster-cloud is installed. Fail early here if not.
-RUN if ! dagster-cloud --version; then \
-        echo "Could not find the dagster-cloud package.  Make sure you include the dagster-cloud package in your project."; \
-        exit 1; \
-    fi
```


## 6. Update the helm values

```yaml
    - name: "k8s-pipeline-1"
      image:
        # When a tag is not supplied, it will default as the Helm chart version.
        repository: "025064823138.dkr.ecr.eu-central-1.amazonaws.com/poc-datapipeline/dagster-pipeline-1"
        tag: local-ltshb-74f2314
...
      # Arguments to `dagster api grpc`.
      # Ex: "dagster api grpc -m dagster_test.test_project.test_jobs.repo -a define_demo_execution_repo"
      # would translate to:
      # dagsterApiGrpcArgs:
      #   - "-m"
      #   - "dagster_test.test_project.test_jobs.repo"
      #   - "-a"
      #   - "define_demo_execution_repo"
      #
      # The `dagsterApiGrpcArgs` key can also be replaced with `codeServerArgs` to use
      # `dagster code-server start` instead of `dagster api grpc`, which can reload its
      # definitions from within the Dagster UI without needing to restart the user code
      # deployment pod.
      dagsterApiGrpcArgs:
        - "--python-file"
        - "/app/src/pipeline_1/definitions.py"
...
```

## Run dagster local

1. Go to the project directory and run `dg dev`

```bash
cd projects/pipeline-1
uv run zsh
dg dev
```
