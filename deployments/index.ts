import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

const clusterStackRef = new pulumi.StackReference("prod");
const kubeconfig = clusterStackRef.getOutput("kubeconfig");
const k8sProvider = new k8s.Provider("prod", {
  kubeconfig: kubeconfig.apply(JSON.stringify)
});

const appName = "streamlit-preview";

const ns = new k8s.core.v1.Namespace(
  appName,
  {
    metadata: {
      name: appName,
      labels: {
        "istio-injection": "enabled"
      }
    }
  },
  { provider: k8sProvider }
);

// const gateway = new k8s.apiextensions.CustomResource(
//   appName,
//   {
//     apiVersion: "networking.istio.io/v1alpha3",
//     kind: "Gateway",
//     metadata: {
//       namespace: deployment.metadata.namespace
//     },
//     spec: {
//       selector: {
//         istio: "ingressgateway"
//       },
//       servers: [
//         {
//           port: {
//             number: 443,
//             name: "https",
//             protocol: "HTTP"
//           },
//           hosts: ["www.aaronbatilo.dev"]
//         }
//       ]
//     }
//   },
//   { provider: k8sProvider }
// );
