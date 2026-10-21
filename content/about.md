+++
title = "About Flashlights"
eyebrow = "About"
lead = "The story, the approach, the name, the licence, and who keeps the lights on."
+++

**Flashlights** is the organisers' portal for events, summits and meetups. It runs the parts of an event nobody in the audience sees: a lightweight speaker intake, the speakers and their files, volunteers and teams, sponsors, the schedule, and the emails that hold it all together.

It was not designed in the abstract. It is derived from the [PyLadiesCon portal](https://github.com/pyladies/pyladiescon-portal), the software built to run PyLadiesCon, a volunteer-run online conference, and it keeps pulling improvements from it. That portal was built for one highly specific purpose, and it is good at it. Its author also organises communities that are nothing like PyLadiesCon, a one-day summit inside a large conference and a monthly meetup chapter among them, and they turned out to need most of the same things: somewhere for speakers to send their files, a team with the right access, sponsors kept track of, a schedule, and the emails. Flashlights is that portal made to serve any of them.

## The approach

Flashlights is for open source communities, meetups and the smaller groups that run events: the ones that need more than spreadsheets and shared documents, and are not the large commercial organisations that can pay for an event management platform. It does not try to be the event platform that works for everything. It keeps the portal's core, turns its identity and its feature switches into configuration, and gives a community two hooks for the rest: a Django app of its own added to the image, and the right to replace a core template or static file. What one community needs and the core does not do lives in that community's repository, not as one more option in the core for everyone. The [Make it yours](/docs/adapt/) page is the practical side of this.

The same line is drawn for running it. Flashlights is software to self-host, one instance per community, on any host that runs a container. Mariatta hosts the instances of the communities she organises; Flashlights itself is not a hosting service. The licence says the same in its own words below: the additional permission is for an organisation's own events, and hosting Flashlights for others falls under the plain AGPL.

## One instance per community

Each community runs its own instance, and each year's event, or each series of dates, is an edition inside it. What the instance is called, its colours, its links and which features it runs are configuration, so the same software serves a three-day online conference and a monthly meetup. A community that needs more than configuration adds its own code to the image without forking the core.

## Still being built

Flashlights is in active development. A community needs more than speaker and sponsor management, and the rest comes step by step, as the communities that run it need it.

## The name

The name comes from the Darren Hayes song *Tiny Little Flashlights*, from the album *Secret Codes and Battleships*. The accent colour is called Beam.

## Licence and contributions

Flashlights is free software under the GNU Affero General Public License version 3, with one additional permission: an organisation may run a modified Flashlights for its own events, including its chapters, departments and member groups, without publishing its changes. Hosting Flashlights as a service for others is not covered by that permission. Code from the PyLadiesCon portal stays under the MIT License, and so does the embeddable program widget.

Flashlights is published for use and study, and does not take code contributions. Bug reports and ideas are welcome as [issues](https://github.com/mariatta/flashlights/issues); a suggestion may be implemented, but code from pull requests is not merged. Report security problems privately, as described in the repository's `SECURITY.md`.

## Who makes it

Flashlights is created and maintained by [Mariatta](/organizers/), a multi-award-winning open source contributor and serial conference organiser.
