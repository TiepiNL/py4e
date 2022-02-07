# Kubernetes cheatsheet

`kubectl version`

## Use the kubectl CLI

`kubectl` requires configuration so that it targets the appropriate cluster. Get cluster information with the following command:
```
kubectl config get-clusters
```

A `kubectl` context is a group of access parameters, including a cluster, a user, and a namespace. View your current context with the following command:
```
kubectl config get-contexts
```

List all the Pods in your namespace.
```
kubectl get pods
```

You can also specify the wide option for the output to get more details about the resource.
```
kubectl get pods -o wide
```

### Create a Pod imperatively

Export a namespace as an environment variable so that it can be used in subsequent commands.
```
export MY_NAMESPACE=sn-labs-$USERNAME
```

Run the `<app_name>` image as a container in Kubernetes.
```
kubectl run <app_name> --image us.icr.io/$MY_NAMESPACE/<app_name>:1 --overrides='{"spec":{"template":{"spec":{"imagePullSecrets":[{"name":"icr"}]}}}}'
```

Describe the Pod to get more details about it.
```
kubectl describe pod <app_name>
```

Delete the Pod.
```
kubectl delete pod <app_name>
```

### Create a Pod with imperative object configuration

Imperatively create a Pod using a configuration file.
```
kubectl create -f <app_name>-create.yaml
```

### Create a Pod with a declarative command

Use the `kubectl apply` command to set a configuration as the desired state in Kubernetes.
```
kubectl apply -f <app_name>-apply.yaml
```

Delete a Pod
```
kubectl delete pod <pod_name>
```

## Load balancing an application
In order to access an application, we have to expose it to the internet using a Kubernetes Service. 
```
kubectl expose deployment/<app_name>
```
This command creates what is called a ClusterIP Service. This creates an IP address that accessible within the cluster.

List Services in order to see that this service was created.
```
kubectl get services
```

Delete the Deployment.
```
kubectl delete deployment/<app_name>
```

## Scaling and Updating Applications
### Scaling the application using a ReplicaSet
Use the `scale` command to scale up your Deployment.
```
kubectl scale deployment <app_name> --replicas=3
```

### Perform rolling updates
Get a status of the rolling update by using the following command:
```
kubectl rollout status deployment/hello-world
```

You can also get the Deployment with the wide option to see that the new tag is used for the image.
```
kubectl get deployments -o wide
```

Kubernetes can roll back the Deployment like this:
```
kubectl rollout undo deployment/hello-world
```

### Using a ConfigMap to store configuration
ConfigMaps and Secrets are used to store configuration information separate from the code so that nothing is hardcoded. It also lets the application pick up configuration changes without needing to be redeployed.

Create a ConfigMap. e.g. one that contains a new message:
```
kubectl create configmap app-config --from-literal=MESSAGE="This message came from a ConfigMap!"
```

Apply a new Deployment configuration:
```
kubectl apply -f deployment-configmap-env-var.yaml
```

Because the configuration is separate from the code, the message - or other variable - can be changed without rebuilding the image. Using the following command, delete the old ConfigMap and create a new one with the same name but a different message.
```
kubectl delete configmap app-config && kubectl create configmap app-config --from-literal=MESSAGE="This message is different, and you didn't have to rebuild the image!"
```

Restart the Deployment so that the containers restart. This is necessary since the environment variables are set at start time.
```
kubectl rollout restart deployment hello-world
```

Delete the Deployment:
```
kubectl delete -f deployment-configmap-env-var.yaml
```

Delete a Service:
```
kubectl delete service hello-world
```



## IBM Labs
- Hands-on Lab: [Introduction to Kubernetes]
- Hands-on Lab: [Introduction to Containers w/ Docker, Kubernetes & OpenShift]
- [Coding project template]

[Introduction to Kubernetes]: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/cc201/labs/2_IntroKubernetes/instructions.md.html
[Coding project template]:    https://github.com/ibm-developer-skills-network/CC201/tree/master/labs/2_IntroKubernetes

[Introduction to Containers w/ Docker, Kubernetes & OpenShift]: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/cc201/labs/3_K8sScaleAndUpdate/instructions.md