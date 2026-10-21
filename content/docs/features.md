+++
title = "Features"
type = "docs"
weight = 20
eyebrow = "Docs"
lead = "A tour of what an instance does, area by area."
+++

## Program

- **Speaker intake.** A lightweight one: people propose a session from their own account, the organisers' queue shows each proposal's state, and a proposed session is approved or declined from its own page. A turned-down proposal can still be approved later. It is not a call for proposals system: there is no scoring and no reviewer assignment. An event that reviews elsewhere invites the speakers it has chosen.
- **Invitations.** Invite a speaker by email; accepting the invitation creates their account. A returning volunteer already has one.
- **Speaker profiles and sessions.** Each presenter has a profile, each session its presenters, and a person speaking twice is one person.
- **Checklists on both sides.** The organisers see what each speaker still owes; the speaker sees the same list from their side, with due dates that follow the talk, and reminders that go out on time.
- **The schedule.** Rooms, slots and sessions, built in an editor and published through a program widget any website can embed and a read-only API.
- **Recordings and uploads.** Videos, slides and other files are kept in a private bucket of yours, next to the session, with a length check on uploaded video.

## People

- **One account per person.** Handles (website, GitHub, Discord, Mastodon, Bluesky, LinkedIn, Instagram, X) and pronouns belong to the account, and every form reads from them.
- **Volunteers.** An application form, a review, and a volunteer hub where speaker checklist items can be assigned to a person or a team.
- **Teams and permissions.** Each team grants permissions from a catalogue, with presets such as Organizers, Program, Sponsorship and Proposal reviewers. Naming a team's leads, and changing what a team grants, are themselves gated by permissions. The settings organisers need left the Django admin.

## Sponsors

- Sponsorship tiers, a prospectus link, contract requests sent to the people who handle them, donations, and the stats that go with them.
- Sponsors never need an account; the organisers keep their record.
- Switch the whole area off for an event that has none, and its pages are gone.

## The numbers

- An organiser dashboard: onboarded volunteers, sponsorship and donations against their goals, attendee count, event tasks and what needs attention.
- Stats pages for attendees (registered, first-timers, demographics when the fields are mapped), sponsorship and volunteers, a year-over-year comparison of registrations, proposals, sponsors and donors, and a JSON feed. Public by default, off with one switch.
- Attendee records come from a Pretix shop through its API or a CSV export of whatever sells your tickets or takes your RSVPs. Flashlights registers nobody and sells no tickets; it keeps the records and counts them.

## Editions

- An edition is one event a year or a series of dates, in person, online or hybrid, with venues and rooms.
- Recordings and community chat are settings of the edition, and the forms follow them.
- Plan the next edition while the current one runs: organisers switch their working edition, speakers and invitation links follow their own.

## Your name on it

- The name, short name, description, logo, favicon, share image, docs link and terms link come from environment variables. Unset, a favicon and a share card are generated from the name and the colour.
- One accent colour, from a preset or a custom value; the ink, hover and press shades are derived. The chrome around it is fixed, so every instance is recognisably Flashlights and recognisably yours.
- Switches turn off volunteering, sponsorship and the public stats.

## Runs anywhere

- Four services: Postgres, Redis, an S3-compatible bucket from any provider (a second, private one when speakers upload files), and SMTP from any provider.
- A boot contract with three processes, `web`, `worker` and `release`, and a production boot that fails at once, naming every missing variable.
- Documented on Heroku and compatible hosts, Azure Container Apps, Cabotage and a plain server. See [Deploy](/docs/deploy/).

## Your own code, without a fork

- A community adds its own Django app to the image, and the app may replace a core template or static file.
- Upgrades are a change of image tag, not a merge. See [Make it yours](/docs/adapt/).

## No third-party code on any page

- Every script, stylesheet, font, icon and chart is served by the instance itself. The only other host a page touches is your own bucket, for the pictures and files people upload.
- No analytics, no advertising, no third-party cookies. The third-party services an instance talks to are on the server side: its bucket and its mail provider, plus Pretix and Sentry when you configure them.

## Documentation per release

- Each release publishes its own version of the [core documentation](https://docs.flashlights.app/latest/), and an instance's help links point at the version it runs.
- A community with docs of its own points the help links there and links back to the core docs at its pinned version.
