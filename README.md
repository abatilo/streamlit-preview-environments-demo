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

Still need:

- Come up with a small streamlit application idea, maybe something with an API
- Need the environment reloader web app. Go web app that receives a webhook
  that will be sent via a GitHub Action and then the webapp will pull the
  branch. Environment reloader will run the streamlit cmd in the background
- Need the GitHub Actions that will provision and deploy the virtual service which fronts the reloader for a given PR/branch

Some change
