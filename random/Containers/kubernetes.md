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

## IBM Labs
- Hands-on Lab: [Introduction to Kubernetes]
- [Coding project template]

[Introduction to Kubernetes]: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/cc201/labs/2_IntroKubernetes/instructions.md.html
[Coding project template]:    https://github.com/ibm-developer-skills-network/CC201/tree/master/labs/2_IntroKubernetes

