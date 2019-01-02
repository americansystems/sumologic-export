# sumologic-export

Easily export your Sumologic log data.

![Box Sketch](https://github.com/americansystems/sumologic-export/raw/master/assets/box-sketch.jpg)

## Purpose

This is a fork of [sumologic-export](https://github.com/rdegges/sumologic-export) created by [@rdegges](https://github.com/rdegges), modernized for our current use cases by [@cafogleman](https://github.com/cafogleman).

`sumologic-export` will grab every single Sumologic log you've ever written
and store it in gzipped JSON files either locally, or in an S3 bucket.

## Installation

To install sumologic-export, make sure you have git, python3 and pipenv installed, then:

    1. git clone https://github.com/americansystems/sumologic-export.git
    2. cd sumologic-export
    3. pipenv install

## Usage

Before you can export all your Sumologic data, you'll need to configure
`sumologic-export` and give it your Sumologic credentials.  To do this,
simply run:

```console
sumologic-export --configure
```

On the command line.  This will prompt you for some basic information, then
store your credentials in the local file `~/.sumo`.

Next, to run a backup job, you can run:

```console
sumologic-export
```

This will export all your Sumologic data for the past month and dump it into a
new directory named `exports`.

If you'd like to specify a custom date range, you can do so by adding a start
and stop date of the form `YYYY-MM-DD`, for instance:

```console
sumologic-export 2018-01-01 2018-06-01
```

Or, if you'd like, you can just specify a start date, and the exporter will
export all logs from the start date till the current day.

```console
sumologic-export 2018-01-01
```

**NOTE**: Depending on how many logs you have, this process may take a while.

Once the process is finished, you'll have an `exports` directory populated with
gzipped JSON files.  There will be one JSON file for each timeslice (defined as a constant), for instance:

```console
$ ls exports
2018-01-01T00:00:00.json.gz
2018-01-02T00:00:00.json.gz
```

If you'd like to export to S3, first make sure you have a default [boto3 profile configured](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html), then use `-b <bucket-name>` to specify where to save

For full usage information, run `sumologic-export -h`.

## Help

Need help?  Can't figure something out?  If you think you've found a bug, please
open an issue on the GitHub issue tracker.

## Changelog

v0.0.3: 2018-12-17

    - Updated for modern usecases, including multithreading and S3 bucket storage

v0.0.2: 2015-01-19

    - Fixing off-by-one error in pagination logic. This was causing us to NOT
      download the last page of logs :(  Thanks
      [@sumoway](https://github.com/sumoway) for the report!

v0.0.1: 2014-06-25

    - First release!  Woo!

## Thanks

Thanks to [@rdegges](https://github.com/rdegges), and [AMERICAN SYSTEMS](https://americansystems.com).