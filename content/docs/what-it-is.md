+++
title = "What Flashlights is"
type = "docs"
weight = 10
eyebrow = "Docs"
lead = "Who it is for, what it runs, and what it leaves to other tools."
+++

Flashlights is the portal your organising team, your volunteers and your speakers sign in to. Attendees have nothing to sign in to. It replaces the dozen spreadsheets an event usually runs on: who proposed what, who was invited, who has sent their slides, who is on which team, who is sponsoring at which tier, what goes in which room when.

## Who it is for

- **A conference or summit** that takes session proposals, invites speakers, and has a schedule with rooms, sponsors and a volunteer team.
- **A meetup or user group** with a series of nights through the year, a venue or two, speakers who need a checklist, and a small organising team.
- **A chapter or department** of a larger organisation that runs its own events and wants its own instance under its own name.

Flashlights does not care which of these you are. One instance serves one community, and each event, or each series of dates, is an edition inside it. Turn off the areas you do not need: an event with no sponsors runs without the sponsorship pages, and one with no volunteer programme runs without the volunteer hub.

## What it runs

- **Program**: proposals, approved or declined one by one, invitations, speaker profiles, sessions, checklists on both sides, the schedule, recordings and uploads, and a public program widget and API.
- **People**: volunteer applications, teams, permissions granted through teams, and one account per person whose handles and pronouns flow into every form.
- **Sponsors**: tiers, contract requests, donations and stats, kept by the organisers.
- **The numbers**: an organiser dashboard and stats pages, fed by the portal's own records and by attendee records read from Pretix or a CSV export.
- **Emails**: the portal's own messages, written once in Markdown and delivered as text and HTML; sign-in and verification codes are plain text.

The [features page](/docs/features/) goes through each area.

## What it leaves to other tools

- **Running a call for proposals.** Flashlights takes session proposals through a simple queue, approved or declined one by one. A large review with scoring and reviewer assignment belongs to Pretalx or Sessionize; the accepted speakers are invited here.
- **Selling tickets.** Flashlights reads who registered from your ticketing or RSVP tool; it is not a ticket shop.
- **Your public website.** Flashlights is the private side. A public program widget and API let your website show the schedule; the rest of the website is yours. [Popular](https://popular.mariatta.ca), a theme for community sites, is built by the same person and is the natural front of house.
- **Video calls and chat.** The edition records where its community chat lives and whether talks are recorded; the calls and the chat happen on the platforms you already use.

## Where it comes from

Flashlights is derived from the [PyLadiesCon portal](https://github.com/pyladies/pyladiescon-portal), which remains the portal built for PyLadiesCon, and keeps pulling improvements from it. The portal was built for one event's needs; Flashlights keeps its core and moves what differs between communities into configuration and each community's own code, instead of growing options for everyone. It is software to self-host, not a hosting service; the [about page](/about/#the-approach) explains the approach. It is free software under the GNU AGPL version 3, with a permission to run a modified copy for your own organisation's events. The [about page](/about/) has the details.

## Reading on

- [Try it](/docs/try-it/): a populated instance on your machine in a few minutes.
- [Deploy](/docs/deploy/): what an instance needs and where it runs.
- [Make it yours](/docs/adapt/): configuration first, your own code when that is not enough.
- The [core documentation](https://docs.flashlights.app/latest/) describes every screen, variable and command, one version per release.
