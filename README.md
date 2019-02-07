# scrapy-splash-demo

## What does it do?
This is a demo project to show the use of Scrapy and Splash for infinite scroll. Specifically, it gets all accordion related tracks from the last week on SoundCloud.

## Requirements
* Docker
* Docker Compose

## Usage
Run:

`docker-compose up`

This will launch both Splash and the spider. The resulting scrapes will be stored in the `scrapes` folder and new items will be persisted to a SQLite database `tracks.db`.
