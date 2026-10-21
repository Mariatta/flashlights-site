+++
title = "Deploy"
type = "docs"
weight = 40
eyebrow = "Docs"
lead = "What an instance needs, where it runs, and how it is kept up to date."
+++

An instance is one image, four services and a set of environment variables. Nothing in the code knows which host you chose.

## The image

Each release publishes `ghcr.io/mariatta/flashlights:X.Y.Z`, a slim image for `amd64` and `arm64`, and `X.Y.Z-full`, which adds machine transcription for uploaded video. `X.Y` and `latest` follow the newest release. Pin a version in production and upgrade on purpose: until 1.0, read the [changelog](/changelog/) entry before you do.

## Four services

| Service | Any provider | Notes |
|---|---|---|
| Postgres | yes, 15 or newer | the database |
| Redis | yes | the queue the worker reads |
| An S3-compatible bucket | yes | speaker uploads; Cloudflare R2, Backblaze B2, DigitalOcean Spaces, MinIO and AWS all work |
| SMTP | yes | every email the portal sends |

## The boot contract

Three processes from one image: `web` serves the site, `worker` sends the emails and processes the uploads, and `release` runs the migrations before a new version takes traffic. Optional processes split the media work and the scheduled reminders out of the worker.

In production the boot fails at once, naming every missing variable, so a misconfigured instance never half-starts. The [environment reference](https://docs.flashlights.app/latest/developer/environment/) lists every variable with its default.

## Hosts

The [deployment guide](https://docs.flashlights.app/latest/developer/deployment/) walks through each of these in the same order: what to create, how the processes map onto the host, how the release step runs, where the logs are, and the host's quirks.

- **Heroku and compatible hosts** (Dokku, Render through its import, and others): `app.json` and `heroku.yml` describe the instance, add-ons included, and a Deploy button creates it.
- **Azure Container Apps**: a Bicep template provisions Postgres, Redis and the container apps from an image tag.
- **Cabotage**: the platform the Python Software Foundation runs.
- **A plain server**: Docker Compose, with your own Postgres and Redis or the containers in the file.

## Your name on it

After the first deploy, set the site domain and the identity variables: the name, the colour, the logo and the links. The [configuration page](/docs/adapt/) is the short version; the environment reference has them all.

## Keeping it up to date

A release is an image tag, a changelog entry and a GitHub release. Upgrading is a change of tag followed by the release step, which runs the migrations. The docs for the version you run are at `https://docs.flashlights.app/X.Y.Z/`, and an instance's own help links already point there.
