Alarm System (py-alarm)

A lightweight, asynchronous alarm and timer manager written in modern Python (3.8+). Built using Python's native `asyncio` library, this package allows you to schedule one-shot timers, recurring alarms, and delayed task execution with minimal resource overhead.

---

## Features

- **Asynchronous & Non-blocking**: Uses `asyncio` event loops for smooth concurrency without freezing your main application.
- **Flexible Scheduling**: Supports single-run countdown timers, daily recurring alarms, and dynamic cron-style scheduling.
- **Custom Callbacks & Handlers**: Trigger any Python callable (async or sync) upon alarm expiration.
- **Audio & Push Notifications**: Integrated cross-platform sound playback and desktop alerts (optional dependencies).
- **Zero Heavy Dependencies**: Runs out of the box with standard Python libraries.
