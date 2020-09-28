# streamlit-preview-environments-demo

I've talked about the idea of doing preview environments before but I wanted an
open source implementation/reference for people to look at.

This workflow is inspired by products like [Heroku's Review
Apps](https://devcenter.heroku.com/articles/github-integration-review-apps) and
[FeaturePeek](https://featurepeek.com/).

I've seen many options for doing things like this with frontend applications
with thin single page apps that are purely hosting a bundle. For example,
performing an `aws s3 sync` to some S3 bucket that's fronted by CloudFront. I
want to demonstrate a more advanced environment that has a backend component to
it.

[Streamlit](https://www.streamlit.io/) is self described as:

```
Streamlit’s open-source app framework is the easiest way for data scientists
and machine learning engineers to create beautiful, performant apps in only a
few hours!
```

I thought this was a perfect example for an application because Streamlit has a
hot reloadable server side feature. It's one thing to just rebuild and redeploy
a container over and over to your feature environment, but that would be a bit
slow because you have to build and push the container over and over again. I
wanted something faster that felt more like the webpack dev server or Flask in
debug mode.

Sometimes there are development environments that are just hard to do locally.
Maybe there's too many containers or in the case of Streamlit specifically, you
might actually be doing machine learning related activities and you only have a
subset of your data available locally. You could extend on this pattern and
deploy your PRs to cloud instances that have GPUs on them. Locally, your
`streamlit` instance will point to your local disk for that subset of data, but
once deployed, your `streamlit` app will download the full data sets from S3.

### How does it work?

#### The environments

The core of how this works is in the [tiny Go
application](cmd/reloader/main.go) that I wrote that clones and pulls the PR
branches. The application is ran with a [few environment
variables](https://github.com/abatilo/streamlit-preview-environments-demo/blob/836712b39f5123e6c4a6c36d6593c2a297ac23dd/cmd/reloader/main.go#L17-L22)
that control which code we run with Streamlit. We
[clone](https://github.com/abatilo/streamlit-preview-environments-demo/blob/836712b39f5123e6c4a6c36d6593c2a297ac23dd/cmd/reloader/main.go#L53-L57)
said repository and branch and then we [run
streamlit](https://github.com/abatilo/streamlit-preview-environments-demo/blob/836712b39f5123e6c4a6c36d6593c2a297ac23dd/cmd/reloader/main.go#L90)
in the configured directory as a goroutine running in the background. We
configure streamlit to expose itself on `0.0.0.0` and enable the
`server.runOnSave` configuration which means that if the running file is
changed, the website will reload itself. The website connects via a WebSocket
from the browser side so that it knows to re-render, so you don't even need to
worry about refreshing the page.

[Building and pushing this reloader](./.github/workflows/reloader.yml) is done
with a GitHub Action and the Docker image is [hosted and
linked](https://github.com/users/abatilo/packages/container/package/streamlit-reloader)
to this repo via GitHub Container Registry.

When a pull request is made, we trigger a [GitHub
Action](./.github/workflows/pr_opened.yml) which performs a helm installation
of the [reloader application's chart](./deployments/chart/), configured with
the repository URL, branch, and relative path as values for the helm release. A
link to your new environment will be added as a
[comment](https://github.com/abatilo/streamlit-preview-environments-demo/pull/5#issuecomment-695368161)
on your pull request.

When a pull request is updated, we [send a
webhook](./.github/workflows/pr_updated.yml) to the deployed reloader which
triggers a `git pull`. If the `main.py` Streamlit app has changed, the
`streamlit` process will reload the application and send your browser an
update.

When a pull request is merged or closed, we [delete the
environment](./.github/workflows/pr_closed.yml) to free up those resources. And
now you have easy and automatic development environments for developers.

#### The backing infrastructure

The `streamlit` instance itself exposes the hosted website on port `:8501`. We
expose the reloader webhook route at `:8080`. We're using an [Istio
VirtualService](https://github.com/abatilo/streamlit-preview-environments-demo/blob/836712b39f5123e6c4a6c36d6593c2a297ac23dd/deployments/chart/templates/virtualservice.yaml#L13-L26)
to handle the route based mapping along with the wildcard subdomain routing for
each environment.

This is running on my own EKS cluster which has heterogenous cluster
autoscaling via [Spot.io](https://spot.io/). So your development team could
have as many branches as you want and you can continue to host all of the
different branches no matter how many concurrent environments there are. That
being said, having something like [stalebot](https://github.com/apps/stale)
might be advised to make sure that PRs don't stay open forever.
