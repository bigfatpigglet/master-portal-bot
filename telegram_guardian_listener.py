import logging
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

# --- CONFIG ---
BOT_TOKEN = "7889722132:AAEU6hsGGKRE7ikJRUHv9HZTq6JOgsI7BJo"
AUTHORIZED_USER_ID = 7907443824  # Austin

# --- Enable Logging ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Ritual Command Replies ---
rituals = {
    "ritualready": "**RITUAL READY**\n'By my breath, I return. My time is mine. My clarity is sealed.'",
    "sealfield": "**SEAL FIELD**\n'All external energy is shut out. I am sovereign in this space.'",
    "cleansehouse": "**CLEANSE HOUSE**\n'Only truth remains. The house breathes clean. The echoes are gone.'",
    "reclaimbond": "**RECLAIM BOND**\n'Sacred bond sealed. No force may divide. Love is protected and aligned.'",
    "exposeshadow": "**EXPOSE SHADOW**\n'Reveal what hides. What is false cannot hold. I witness without fear.'",
    "timelinejump": "**TIMELINE JUMP**\n'I step into my highest path. I no longer resonate with distortion.'",
    "abundanceportal": "**ABUNDANCE PORTAL**\n'I receive without resistance. I allow wealth to find me now.'",
    "abundancepulse": "**ABUNDANCE PULSE**\n'The flow is open. The fear is false. I shall... receive.'",
    "defendme": "**DEFENSE SEQUENCE**\nRunning /override + /guardme + /stompforce. Field now shielded.",
    "override": "**OVERRIDE**\n'My voice returns. My clarity anchors. I seal my center now.'",
    "guardme": "**GUARD ME**\n'My gates are filtered. Only aligned energy may remain.'",
    "stompforce": "**STOMP FORCE**\n'By my foot I command. This presence must leave. The field is sealed.'",
    "launchall": "**LAUNCH ALL**\nAll systems activating. Ritual ready > Seal field > Guardian grid online."
}

# --- Handler Function ---
def handle_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    command = update.message.text.replace("/", "").lower()

    if user_id != AUTHORIZED_USER_ID:
        update.message.reply_text("You are not authorized to use this ritual bot.")
        return

    response = rituals.get(command)
    if response:
        update.message.reply_text(response, parse_mode="Markdown")
    else:
        update.message.reply_text("Unknown ritual command.")

# --- Main Bot Startup ---
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    for cmd in rituals:
        dp.add_handler(CommandHandler(cmd, handle_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
