# streamlit-preview-environments-demo

I've talked about the idea of doing preview environments before but I wanted an
open source implementation/reference for people to look at.

This workflow is inspired by products like [Heroku's Review
Apps](https://devcenter.heroku.com/articles/github-integration-review-apps) and
[FeaturePeek](https://featurepeek.com/).

I've seen many options for doing things like this with frontend applications
with thin single page apps that are purely hosting a bundle. For example,
performing an `aws s3 sync` to some S3 bucket that's fronted by CloudFront. I want to demonstrate a more advanced environment that has a backend component to it.
