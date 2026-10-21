+++
title = "Make it yours"
type = "docs"
weight = 50
eyebrow = "Docs"
lead = "Configuration first. Your own code when that is not enough. A fork never."
+++

## Configure

Most of what makes an instance yours is environment variables, read at boot:

- **Identity**: `SITE_TITLE`, `SITE_SHORT_NAME`, `SITE_DESCRIPTION`, and the absolute URLs `SITE_LOGO`, `SITE_FAVICON` and `SITE_OG_IMAGE`. Unset, a favicon and a share card are generated from the title and the colour.
- **Colour**: `BRAND_PRESET`, one of `beam`, `teal`, `copper`, `indigo` or `raspberry`, or `BRAND_PRIMARY` with your own `#rrggbb`. The ink on it, its text shade and the hover and press shades are derived.
- **Links**: `DOCS_URL` for your community's own documentation, `TERMS_URL` for your terms of service. The code of conduct, the sponsorship prospectus and the schedule link belong to the edition and are set in the portal.
- **Switches**: `VOLUNTEERING_ENABLED`, `SPONSORSHIP_ENABLED` and `STATS_PUBLIC`. Off, the area's pages are gone and its navigation with them.
- **Contacts**: `SPONSORSHIP_EMAIL` and `ACCOUNTING_EMAIL`, who receives a sponsorship contract request.

Everything else organisers need is set inside the portal: editions, venues and rooms, teams and their permissions, checklist templates, the code of conduct and prospectus links. The [adapting guide](https://docs.flashlights.app/latest/user/adapting/) in the core documentation goes through what you can change without code.

## Add your own code

When configuration is not enough, a community adds a Django app to the core image instead of forking it. The `EXTRA_APPS` variable names the apps; they load first, their templates and static files win over the core's, and their URLs are included under a prefix. An app can add pages, models and migrations of its own, and may replace a core template or static file.

The usual shape is a small repository of your own: a Dockerfile `FROM` a pinned core image, your app, your deployment manifests and your docs. Upgrading the core is a change of tag. The [community apps guide](https://docs.flashlights.app/latest/developer/community_apps/) is the public API your app may rely on, and what changes to it look like in the changelog.

## Document what you changed

If your instance has features or screens of its own, your users need your docs for those and the core docs for the rest. Point `DOCS_URL` at yours, and link from there to the core documentation at the version you pinned, `https://docs.flashlights.app/X.Y.Z/`. Replacing a core template means documenting that screen. The adapting guide says how.

## Why not a fork

Flashlights itself is a fork, of the PyLadiesCon portal, and every sync with it is a merge with conflicts. That is the experience a community should not have to repeat. Configuration and an app of your own give you a portal that is yours, on a core that keeps improving underneath it.
