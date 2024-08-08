# Telegram Bot for GIF Search

This script sets up a Telegram bot that responds to user messages with GIFs related to their queries. It uses the Giphy API to fetch GIFs and the `aiogram` library for bot functionality.

## Code Overview

### Imports

The script imports the necessary modules and libraries:

```python
import time
import logging
import requests
import random
import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram import executor
