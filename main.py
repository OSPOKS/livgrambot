# Copyright 2022 thajudheen

#   Licensed under the Apache License, Version 2.0 (the "License");

 #  you may not use this file except in compliance with the License.

 #  You may obtain a copy of the License at

 #      http://www.apache.org/licenses/LICENSE-2.0

  # Unless required by applicable law or agreed to in writing, software

  # distributed under the License is distributed on an "AS IS" BASIS,

  # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

#   See the License for the specific language governing permissions and

#   limitations under the License.### 
from telegram.ext import Updater

from handlers import setup_dispatcher
from settings import TELEGRAM_TOKEN, HEROKU_APP_NAME, PORT

# Setup bot handlers
updater = Updater(TELEGRAM_TOKEN)

dp = updater.dispatcher
dp = setup_dispatcher(dp)

# Run bot
if HEROKU_APP_NAME is None:  # pooling mode
    print("Can't detect 'HEROKU_APP_NAME' env. Running bot in pooling mode.")
    print("Note: this is not a great way to deploy the bot in Heroku.")

    updater.start_polling()
    updater.idle()

else:  # webhook mode
    print(f"Running bot in webhook mode. Make sure that this url is correct: https://{HEROKU_APP_NAME}.herokuapp.com/")
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"https://{HEROKU_APP_NAME}.herokuapp.com/{TELEGRAM_TOKEN}"
    )

    updater.idle()
