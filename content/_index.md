+++
title = "Home"

[hero]
  eyebrow = "Free software for the people who run events"
  title = "The organisers' side of your event, in one place"
  lead = "Flashlights runs the parts of an event nobody in the audience sees: session proposals, speakers and their files, volunteers and teams, sponsors, the schedule, and the emails that hold it all together. One instance serves one community, edition after edition."
  image = "images/lights.svg"
  [[hero.ctas]]
    label = "Try it on your machine"
    url = "/docs/try-it/"
    icon = "fa-solid fa-lightbulb"
    variant = "primary"
  [[hero.ctas]]
    label = "What it does"
    url = "/docs/features/"
    variant = "outline"
  [[hero.ctas]]
    label = "Source on GitHub"
    url = "https://github.com/mariatta/flashlights"
    icon = "fa-brands fa-github"
    variant = "ghost"

[[stats]]
  value = "1"
  label = "instance per community, an edition per event"
[[stats]]
  value = "4"
  label = "services to run it: Postgres, Redis, a bucket, SMTP"
[[stats]]
  value = "0"
  label = "third-party scripts, fonts, trackers or cookies"
[[stats]]
  value = "AGPL"
  label = "free software, with a permission for your own events"

[featuresHead]
  eyebrow = "What it runs"
  title = "Everything between the idea and the opening session"
  lead = "Built from running real conferences and meetups, and derived from the portal that runs PyLadiesCon. Every part exists because an organising team needed it."

[[features]]
  icon = "fa-solid fa-microphone-lines"
  title = "Session proposals and speakers"
  body = "A simple proposal queue, invitations, speaker profiles, sessions, and two-sided checklists with reminders, so a speaker always knows what you still need from them. Not a call for proposals system: an event that reviews in Pretalx or Sessionize invites its accepted speakers here."
[[features]]
  icon = "fa-solid fa-calendar-days"
  title = "The schedule"
  body = "Rooms, slots and sessions, with recordings and uploads kept with them, plus a public program widget and API your website can read."
[[features]]
  icon = "fa-solid fa-people-group"
  title = "Volunteers and teams"
  body = "Applications, teams, and permissions granted through teams from one catalogue, with presets such as Organizers, Program and Sponsorship. No Django admin for the settings organisers need."
[[features]]
  icon = "fa-solid fa-handshake"
  title = "Sponsors"
  body = "Tiers, contract requests, donations and their stats, kept by the organisers. Sponsors never need an account. Switch the whole area off for an event that has none."
[[features]]
  icon = "fa-solid fa-chart-column"
  title = "The numbers"
  body = "An organiser dashboard with volunteers, sponsorship and donations against their goals, and attendee counts read from Pretix or a CSV export of whatever takes your registrations. Public stats pages with a year-over-year comparison, off with one switch. Flashlights registers nobody; it keeps the records."
[[features]]
  icon = "fa-solid fa-layer-group"
  title = "Editions"
  body = "One event a year or a series of dates, in person, online or hybrid, with venues and rooms. Plan the next edition while the current one runs."
[[features]]
  icon = "fa-solid fa-palette"
  title = "Your name on it"
  body = "The name, colours, logo, favicon, share image and policy links come from environment variables. One image serves any community, and the design system restyles every page."
[[features]]
  icon = "fa-solid fa-server"
  title = "Runs on any host"
  body = "A plain container with a boot contract: web, worker, release. Heroku and compatibles, Azure Container Apps, Cabotage or a plain server, each documented."
[[features]]
  icon = "fa-solid fa-puzzle-piece"
  title = "Your own code, without a fork"
  body = "A community adds a Django app to the image and may replace a core template or static file. Upgrade by bumping the image tag, not by merging."
[[features]]
  icon = "fa-solid fa-envelope"
  title = "The emails"
  body = "Invitations, reminders, notices and the rest of the portal's own emails, each written once in Markdown and sent as text and HTML, through any SMTP provider. Sign-in and verification codes come from the account system as plain text."
[[features]]
  icon = "fa-solid fa-shield-halved"
  title = "No third-party code on any page"
  body = "Every script, stylesheet, font and chart is served by the instance itself. No analytics, no advertising, no third-party cookies. The only other host a page touches is your own bucket, for the pictures and files people upload."
[[features]]
  icon = "fa-solid fa-book"
  title = "Documentation per release"
  body = "Each release publishes its own version of the docs, and an instance's help links point at the version it runs."

[team]
  eyebrow = "Maintainers"
  title = "Who makes Flashlights"
  lead = "Flashlights is published for use and study, maintained by one person, and does not take code contributions. Bug reports and ideas are welcome as issues."
  cta = "Maintainers"

[getInvolved]
  eyebrow = "Try it"
  title = "A populated instance on your machine in a few minutes"
  lead = "Clone, start the containers, load the sample data, sign in as an organiser. That is the demo: the whole organiser side, with nobody watching."
  [[getInvolved.ctas]]
    label = "Try it"
    url = "/docs/try-it/"
    variant = "primary"
  [[getInvolved.ctas]]
    label = "Deploy it"
    url = "/docs/deploy/"
    variant = "outline"
+++
