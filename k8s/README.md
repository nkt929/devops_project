#```kubectl get pods,svc``` output
```NAME                              READY   STATUS    RESTARTS   AGE
NAME                          READY   STATUS    RESTARTS   AGE
pod/devops-79cc676c85-zk6n5   1/1     Running   0          7m5s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/devops       LoadBalancer   10.106.165.235   <pending>     8080:30352/TCP   6m1s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          12m
```

#```kubectl get pods,svc``` output after deployment using configuration files
```
NAME                          READY   STATUS    RESTARTS   AGE
pod/devops-5cc9844458-42bmw   1/1     Running   0          54s
pod/devops-5cc9844458-l947q   1/1     Running   0          54s
pod/devops-5cc9844458-pp4k7   1/1     Running   0          54s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/devops       ClusterIP   10.104.114.174   <none>        5000/TCP   47s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    108m
```
#```kubectl get pods,svc``` output after deployment using Helm
```
NAME                          READY   STATUS    RESTARTS   AGE
pod/devops-8477d9fb84-59rb4   1/1     Running   0          9s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/devops       LoadBalancer   10.101.185.155   <pending>     5000:30310/TCP   34s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          159m
```
# How to use:
```
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```
# How to use Helm:
```
helm package devops
helm install devops ./devops-0.1.0.tgz 
helm upgrade devops ./devops-0.1.0.tgz   
```