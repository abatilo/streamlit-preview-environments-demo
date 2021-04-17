import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

const clusterStackRef = new pulumi.StackReference("prod");
const kubeconfig = clusterStackRef.getOutput("kubeconfig");
const k8sProvider = new k8s.Provider("prod", {
  kubeconfig: kubeconfig.apply(JSON.stringify),
});

const appName = "streamlit-preview";

const ns = new k8s.core.v1.Namespace(
  appName,
  {
    metadata: {
      name: appName,
    },
  },
  { provider: k8sProvider }
);
