# Smartlock Manager - Python Edition

This app was originally written in Node Express: [see here](https://github.com/zanenkn/smartlock-manager).

## About

This application is designed to handle webhooks from the [SimplyBook.me](https://simplybook.me/en/) booking system and integrates with various external APIs to manage access codes for bookings. When a booking is created, updated, or canceled, the application generates a time-bound access code valid only during the booking's active period. This code is then sent to a smart lock IoT device via WiFi bridge, enabling secure, time-limited access. Clients are also notified by email with the access code and booking details.
