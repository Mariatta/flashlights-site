+++
title = "Try it"
type = "docs"
weight = 30
eyebrow = "Docs"
lead = "A populated instance on your own machine, with the organiser side open to you. That is the demo."
+++

There is no hosted demo, on purpose. An event portal only means something with people and roles in it, and the interesting side is the organisers', which cannot be handed to strangers on a shared instance. On your own machine you get all of it.

## What you need

- Docker with Docker Compose
- GNU Make
- Git

## Run it

```sh
git clone https://github.com/mariatta/flashlights.git
cd flashlights
make serve
```

Open <http://localhost:8000/>. The instance is empty; give it a domain and fill it:

```sh
make manage set_site_domain localhost:8000
make seed
```

`make seed` runs `seed_dev_data`: an active edition and a past in-person one, volunteers on teams, speakers at every stage of their checklist, proposals in each state, sponsors and affiliations. It prints the logins when it finishes. Organiser and volunteer accounts use the password `password123`; speaker accounts sign in with a code, which arrives in the local mail viewer at <http://localhost:1080/>.

Sign in as an organiser and open **Organize**. Then sign in as a speaker and see the same event from their side.

## What to look at

- **Organize, Speakers**: the proposal queue, the invitations, each speaker's checklist.
- **Organize, Schedule**: the editor, and the program widget it feeds.
- **Organize, Teams**: who may do what, and where that comes from.
- **Sponsorship** and **Stats**: on by default, each off with one variable.
- **The account page**: handles and pronouns, stored once and shared by every form.

## Going further

The [setup guide](https://docs.flashlights.app/latest/developer/setup/) in the core documentation covers running without Docker, object storage against a local MinIO, the speaker sample data in detail and the tests. The [user guide](https://docs.flashlights.app/latest/user/get_started/) says what each part of the portal does and which parts a small event can skip.

When it does what you need, [deploy it](/docs/deploy/).
