# Dream

Simple Flask Python API as a example\*.

Stack:

-   Python 3.8
-   Flask
-   ArangoDB
-   Docker, Kubernetes & Helm

(\*) And with a true solution

```shell
$ pipenv install
$ pipenv shell
$ python main.py
```

**Minsky Enviroment Deployment**

```bash
$ docker build .
$ export IMAGE=<your-image-id>
$ docker image tag $IMAGE docker.minsky.cc/dreamer
$ docker push docker.minsky.cc/dreamer
$ helm update dreamer ./dreamer
```
